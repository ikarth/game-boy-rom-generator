# Description

## Running the generator
- Initialize paths and random number generator
- Create a Python namespace to hold project data, including basic settings for GB Studio, UI icons, and so on.
- Load assets from asset folder
  - GB Studio stores assets in a folder structure, we replicate that arrangement here
  - Spites, backgrounds, and so on are loaded and appended to the lists of assets by type.
    - The generator has a number of functions (makeSpriteSheet, makeBackground, makeElement, etc.) that take the filename and some parameters that can't be inferred directly from the asset. The functions assemble the database records that will eventually be written out to the GB Studio project file as JSON.
    - these can be called as needed, in any order, acting as a de-facto command language
    - the makeScene() function is the lynchpin of this, reflecting GBS's scene-based model of RPGs.
      - you call makeScene(), then you add actors, sprites, collisions, and triggers to it with the other functions.
    - the addSymmetricSceneConnections() is a special-case of adding a trigger to the scene; it adds triggers to two scenes that establish two-way travel between them.
- Do a final pass to translate references to other scenes into references that use the final scene ID
- Write out the project file description as JSON file in a format that is compatible with GB Studio's .gbproj project save file format.

That's the basic example project generator. Other parts of the project add new generative operations that combine these building blocks into more sophisticated constructions:
- scene generators that create more complex scenes
- scripting
- extracting scenes from existing GB Studio projects and turning them into templates for the generator   
- extracting GB Studio's internal scripting language and translating it into Python commands for the generator
- generating titles and title screens
