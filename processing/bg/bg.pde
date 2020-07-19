color black = #071821; //GBStudio palette colors
color darkGrey = #306850;
color lightGrey = #86c06c;
color white = #e0f8cf;
color yellow =   #ffff00; //Cursor color
color currentColor = #071821; //variable keeping track of current selected color

int tile = 64;
int tilemap = 360;                      //Max number of background tiles that can fit on screen at once is 360...
int maxTiles = 192;                     //...but GB Studio only supports 192 unique tiles at a time :(
int[][] tiles = new int[tilemap][tile]; //2d array containing all pixels onscreen. 1st value picks tile from tilemap, second value picks pixel from tile.
boolean isMatching = false;             //bool to test if two tiles match.
boolean isUnique = true;                //bool to mark if a tile is unique.
int uniqueTiles = 0;                    //a count of the number of unique tiles in the image.
int selected;                           //variable to register the selected tile in the tilemap.
int copy;                               //variable to register the tile to copy.
int xClick = 0;                         //variable to save the x coordinates of the mouse when clicked.
int yClick = 0;                         //variable to save the y coordinates of the mouse when clicked.
boolean display = false;

String filename1 = "static";  //File name information.
int saveNum = 1;
String filename2 = ".png";

void keyPressed() {
  if (key == 'p') {                          //If the key is p...
    drawImage();
    save(filename1 + saveNum + filename2);   //print a PNG of the current state...
    saveNum++;                               //and change the filename so you don't overwrite it next time.
  }
  if (key == 'o') {                          //If the key is o...
    if (display == true) {                   //If display is on,
      display = false;                       //Turn it off!
    } else {                                 //But if it's off...
      display = true;                        //Turn it on!
    }
  }
  if (key == 'c')                            //If the key is c...
    copy = selected;                         //save the selected tile as the copied tile.
  if (key == 'v')                            //If the key is v...
    replace(selected, copy);                 //replace the selected tile with the copied tile.
  if (keyCode == LEFT && selected > 0) {      //If the key is LEFT (and the cursor isn't on the first tile)...
    display = true;                         //Turn on display
    selected--;                              //Move cursor to the left.
  }
  if (keyCode == RIGHT && selected < 359) {    //If the key is RIGHT (and the cursor isn't on the last tile)...
    display = true;                         //Turn on display
    selected++;                              //Move cursor to the right.
  }
  if (keyCode == UP && selected > 19) {       //If the key is UP (and the cursor isn't on the first row)...
    display = true;                         //Turn on display
    selected = selected - 20;                //Move the cursor up a row.
  }
  if (keyCode == DOWN && selected < 340) {    //If the key is DOWN (and the cursor isn't on the last row)...
    display = true;                         //Turn on display
    selected = selected + 20;                //Move the cursor down a row.
  }
}

void setup() {                         //Initialization of the program.
  size(160, 144);                      //Initial size
  colorMode(RGB);                      //Determines color mode.
  //strokeWeight(2);                   //Sets line stroke to two pixels wide. 
  //surface.setResizable(true);        //The view window is resizeable.
  for (int i = 0; i < tilemap; i++) {  //For each tile in the tilemap...
    newTile(i);                       //Create a new tile.
  }
  for (int i = 0; i < tilemap; i++) {  //For each tile in the tilemap...
    checkMatch(i);                     //Check if it matches any other tiles.
    if (uniqueTiles > maxTiles) {      //If there are more unique tiles than max tiles...
      replace(i, int(random(192)));    //Replace the new unique tile with a random tile...
      uniqueTiles--;                   //and decrease the number of unique tiles by one.
    }
  }
}

void newTile(int i) {                //Create a new tile with random pixel values.
  for (int j = 0; j < tile; j++) {   //For each pixel in the tile...
    tiles[i][j] = int(random(4));    //Choose a random color.
  }
}

void chooseColor(int col) {                  //Function to convert a number from 0-3 into a GB-safe color
  switch(col) {                              //Assign a color for each number
    case 0: currentColor = black; break;
    case 1: currentColor = lightGrey; break;
    case 2: currentColor = darkGrey; break;
    case 3: currentColor = white; break;
  }
  //print(col + " ");                          //Print color
}

void checkMatch(int t) {                //Function to check if a tile matches any other tiles.
  for (int i = 0; i < tilemap; i++) {   //For each tile in the tilemap...
    if (i != t) {                       //(except for the chosen tile itself)
      compareTiles(i, t);               //compare the tile to the chosen tile,
      if (isMatching == true) {         //and if it matches one of them,
        isUnique = false;               //mark it as not unique.
      }
    }
  }
  if (isUnique == true)                 //If it still registers as unique after the check,
    uniqueTiles++;                      //Increase the count of unique tiles by one.
}

void compareTiles(int t1, int t2) {      //Function to compare two tiles to see if they match.
  isMatching = true;                     //First, suppose that the two tiles match.
  for (int j = 0; j < tile; j++) {       //For each pixel in the tile...
    if (tiles[t1][j] != tiles[t2][j]) {  //if any pixel in the same position doesn't match,
      isMatching = false;                //mark the tiles as not matching.
    }
  }
  //print(isMatching + "\n");
}

void replace(int t1, int t2) {          //Function to replace the tile in the 1st argument with the tile in the 2nd argument.
  for (int j = 0; j < tile; j++) {      //For each pixel in the tile...
    tiles[t1][j] = tiles[t2][j];        //replace the pixel in the 1st tile with the pixel in the 2nd tile.
  }
}

void mouseClicked() {                   //When the mouse is clicked,
  display = true;
  select();                             //select that tile.
}

void select() {                          //Function to select a tile using the mouse.
  print(mouseX + ", " + mouseY + "\n");  //Check the location of the mouse in console.
  int x = mouseX / 8;                    //x coordinate of the selected tile.
  int y = mouseY / 8;                    //y coordinate of the selected tile.
  selected = (y * 20) + x;               //Convert these coordinates to the tilemap value.
  print(x + ", " + y + "\n");            //Print tile coordinates
  print(selected + "\n");                //Print tilemap value
}

void selectDraw() {                      //Function to add a border to the selected tile.
  noFill();                              //Don't fill the rectangle.
  stroke(yellow);                        //Make rectangle just a yellow border.
  rect((selected * 8 % 160)-1, (selected / 20 * 8)-1, 9, 9);  //Determine x and y coordinates of rectangle from selected tilemap value.
}

void drawImage() {                           //Draw the image
  for (int i = 0; i < tilemap; i++) {        //For each tile in the tilemap...
    for (int j = 0; j < tile; j++) {         //and for each pixel in that tile...
      chooseColor(tiles[i][j]);              //choose a color based on the assigned value for that pixel,
      int x = int(j % 8) + (int(i % 20) * 8);//determine the x coordinate of the pixel
      int y = int(j / 8) + (int(i / 20) * 8);//determine the y coordinate of the pixel
      set(x, y, currentColor);               //and draw the pixel!!
      //set(x, y + 72, currentColor);
    }
  }
}

void draw() {
  //scale(2.0);  //This should scale the whole image but it isn't working right >:(
  drawImage();                                 //Draw the image
  if (display == true)                         //If display in on...
    selectDraw();                              //Draw the selected tile.
}

/*void newMapPrototype() {
  for (int i = 0; i < tilemap; i++) {
    for (int j = 0; j < tile; j++) {
      tiles[i][j] = int(random(4));
      print(tiles[i][j]);
    }
    print("\n");
  }
}*/