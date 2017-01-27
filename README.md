# Turpenscape
**Turpenscape** allows designers to create Inkscape (and Gimp!) palettes from an image. It will extract the most prominent colors of the uploaded image and will return a palette file `GPL` that can be read by inkscape.

![Using Turpenscape](http://i.imgur.com/CK6Kg4H.jpg)

![Turpenscape result](http://i.imgur.com/E74CSbz.jpg)

## Why Turpenscape?
Turpenscape can be very useful to create palettes from images. Designers, looking for inspiration, use images from paintings or photographs to find the colors that fit into their design.

Soon, we will add some example palettes from great artists!  

## How do I install a palette in Inkscape?

Installing a palette its a very simple process that can be carried out using your File Manager

1. Generate a palette from the app or download one of our references. Remember to type a memorable palette name.
2. Copy the individual `GPL` files into your Inkscape config folder under the `palettes` folder. If it's not there, create it.

    - For Linux and OS X: the local user directory is `~/.config/inkscape/palettes`
    - For Windows: Copy the file under
        - `%PROGRAMFILES%\Inkscape\share\palettes`. (64 bits)
        - `%PROGRAMFILES(x86)%\Inkscape\share\palettes`. (32 bits)

3. Launch Inkscape (close it first if it's already running).
4. Find the palettes list at the bottom-right part of your screen. You should see your palette in the dropdown.

## How can I contribute?
Please fill out an issue and provide a image reference before any pull request. Discussion should be open.

## How to create my palette from the Inkscape UI?
That's great too! Although this is not the repo you are looking for. You should totally read [how to create custom color palettes in inkscape](http://goinkscape.com/custom-color-palettes-in-inkscape/)
