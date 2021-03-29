import numpy as np
import matplotlib.pyplot as plt
import imageio
import base64
import IPython.display
from tqdm import tqdm
import random
import retro
retro.__version__



#
# def show_movie(frames):
#   imageio.mimwrite('last.mp4', np.array(frames), fps=60)
#   return IPython.display.HTML("""
# <video width=512 controls autoplay><source src="%s" type="video/mp4"></video>
# """ % ("data:video/mp4;base64," + base64.b64encode(open('last.mp4','rb').read()).decode()))

#plt.show()


"""# Run exploration"""

def runExploration(rom_path=r"J:\Isaac\Dev\genboy\gbprojects\generated\LegendofMagicWaxOutlaw\build\web\rom\game.gb", movie_output_path="."):

    print("### Running Automatic Exploration ###")

    emu = retro.RetroEmulator(rom_path)
    gamedata = retro.data.GameData()
    emu.configure_data(gamedata)
    emu.set_button_mask([0]*9,0)
    boot_state = emu.get_state()

    {hex(k): len(v) for k,v in gamedata.memory.blocks.items()}

    gamedata.valid_actions()

    a = sum([action[-1] for action in gamedata.valid_actions()])
    [(a>>i)&1 for i in range(9)]

    # for i in range(100):
    #   emu.step()

    #plt.imshow(emu.get_screen());
    #plt.imshow(emu.get_screen()[:,:,0].reshape(9,16,10,16).mean((1,3)).astype(int) & 0xf0,cmap='gray');

    def current_cell():
      screen = emu.get_screen()
      #return (screen[:,:,0].reshape(9,16,10,16).mean((1,3)).astype(int) & 0xc0).astype('uint8').tobytes()
      return (screen[:,:,0].reshape(9,16,10,16).mean((1,3)).astype(int) & 0xfc).astype('uint8').tobytes()
      #addr = 0xff80
      #addr = 0x8000
      #addr = 0xfe00
      #return hash((np.frombuffer(gamedata.memory.blocks[addr],dtype='uint8') & 0xfc).tobytes())

    def sample_random_action():
      return sum([random.choice(choice) for choice in gamedata.valid_actions()])


    NUM_ITERATIONS = 50000#0#0
    STEPS_PER_ITERATION = 15*60
    STICKY_RATE = 0.975

    random.seed(98795)

    archive = {}

    emu.set_state(boot_state)
    emu.step() # so that frame will be current
    boot_screen = emu.get_screen()
    boot_cell = current_cell()

    archive[boot_cell] = {
        'trajectory': [],
        'state': boot_state,
        'visits': 1
    }
    progress_over_time = []

    with tqdm(desc='new cells') as new_cells:
      for iteration in tqdm(range(NUM_ITERATIONS),desc='iterations'):

        # pick a cell
        probabilities = [1.0/np.sqrt(v['visits']) for v in archive.values()]
        chosen_cell = random.choices(list(archive.keys()),weights=probabilities,k=1)[0]
        #chosen_cell = random.choice(list(archive.keys()))

        # go to the cell
        emu.set_state(archive[chosen_cell]['state'])
        archive[chosen_cell]['visits'] += 1

        # local exploration from this cell
        trajectory = archive[chosen_cell]['trajectory'].copy()

        action = sample_random_action()

        for step in range(STEPS_PER_ITERATION):

          if random.random() > STICKY_RATE:
            action = sample_random_action()

          trajectory.append(action)
          emu.set_button_mask([(action>>i)&1 for i in range(16)], 0)
          emu.step()

          cell = current_cell()

          if cell not in archive or len(trajectory) < len(archive[cell]['trajectory']):
            if cell not in archive:
              new_cells.update(1)
            archive[cell] = {
                'trajectory': trajectory.copy(),
                'state': emu.get_state(),
                'visits': 0
            }
          archive[cell]['visits'] += 1
          progress_over_time.append(len(archive))

          if archive[cell]['visits'] > 1 + archive[chosen_cell]['visits'] and random.random()>0.90:
            break

    print(len(archive), 'cells reached')

    plt.plot(progress_over_time);
    progress_over_time[-1]/len(progress_over_time)
    plt.savefig(movie_output_path + "/progress.png")
    plt.figure()
    plt.hist([v['visits'] for v in archive.values()],bins=100,log=True);
    plt.savefig(movie_output_path + "/visits.png")
    #plt.figure()
    plt.hist([len(v['trajectory']) for v in archive.values()],bins=100,log=True);
    plt.savefig(movie_output_path + "/trajectory.png")
    plt.figure()


    longest_trajectory = max([v['trajectory'] for v in archive.values()], key=len)
    longest_screens = []
    emu.set_state(boot_state)
    for action in tqdm(longest_trajectory):
      emu.set_button_mask([(action>>i)&1 for i in range(16)], 0)
      emu.step()
      longest_screens.append(emu.get_screen())

    #res = show_movie(longest_screens)

    imageio.mimwrite(movie_output_path + '/explore.mp4', np.array(longest_screens), fps=60)

if __name__ == '__main__':
    runExploration()
