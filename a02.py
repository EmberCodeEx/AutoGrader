
### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(length, width):
    return length * width

#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_length, plot_width, tile_length, tile_width):
    plot_area = calculateArea(plot_length, plot_width)
    tile_area = calculateArea(tile_length, tile_width)
    if plot_area % tile_length == 0.0 and plot_area % tile_width == 0.0 and plot_length > 0 and plot_width > 0 and tile_length > 0 and tile_width > 0:
        return True
    else: 
        return False

#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_length, plot_width, tile_length, tile_width):
    if type(plot_length) == str or type(plot_width) == str or type(tile_length) == str or type(tile_width) == str:
        return "Invalid Input"
    elif plot_length == 0 or plot_width == 0 or tile_length == 0 or tile_width == 0:
        return None
    plot_area = calculateArea(plot_length, plot_width)
    tile_area = calculateArea(tile_length, tile_width)
    number_of_tiles = plot_area // tile_area
    print(number_of_tiles)
    tiles_fit = checkTilesFit(plot_length, plot_width, tile_length, tile_width)
    print(tiles_fit)
    if type(number_of_tiles) == int and tiles_fit == True:
        return number_of_tiles
    else:
        return "Not Possible"

#### End OF MARKER



