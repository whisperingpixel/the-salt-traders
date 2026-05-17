# The Salt Traders in Medieval Salzburg

The Salt Traders · A merchant simulation game of the medieval salt trade. The purpose is for teaching in the "Basics of Software Development" class with a focus on spatial data.

## About

This program is part of the exercise class "Practice Software Development" at the Department of Geoinformatics (University of Salzburg) in Summer 2026. It consists of several parts that build upon each other. The programming language for teaching this excesise is Python, although this is not explicitly a Python programming class.

Background: The medieval salt trade was the foundation of Salzburg's wealth and power. Salt was often referred to as "white gold" and heavily influenced the region's art, particularly under the rule of the prince-archbishops. Significant amounts of salt were mined, especially in Dürrnberg, but also partly in Berchtesgaden. The salt was transported along the Salzach River to downstream cities, including Salzburg, Laufen, and Passau.

Step into the footsteps of a medieval merchant and build your salt trading business.

Note: The salt trade represented here is largely simplified. The complexity increases in each part but will remain simplified for teaching purposes.

## Prerequisites

These lessons expect a basic knowledge of a programming / scripting language. In the class "Practice Software Development" this has been covered in the first sessions. The expectations are:

- Declaring / initialising variables
- Data types
- Lists / dictionaries
- For and while loops

## Lessons

The lessons are organised in the corresponding subfolders and each lesson builds upon the previous one. Therefore, there are at least two files in each subfolder: The file with the `_ex_` in the filename is the exercise file. In this file a learning outcome corresponds with at least one TODO. This TODO indicates that there is something new to implement. An example solution is provided in the second file. For the continuation of the exercise, you can either continue to use your own file or use the execise-files provided in the individual folders.

At the bottom of each file are either optional improvements or assignments. The optional improvements can be done on your own and are mostly additional exercises for of the same topic / learning outcome.

Part / Lesson | Expected learning outcomes
---------|-------------------
 1 | Creating and using functions in Python.
 2 | File handling, YAML configuration files, handling errors and exceptions, documentation
 3 | Passing arguments to the program, command-line interfaces
 4 | Creating and instantiating classes, using class methods
 5 | Class inheritance, composition
 6 | Geospatial vector data
 7 | Geospatial raster data
 8 | Coordinate systems and coordinate transformation
 9 | Finalisation and playing the game

## Trade-offs and special cases

The lessons aim to create smaller learning units with clear milestones that include runnable code and meaningful output. Although Python is used as the language for teaching, the goal is not to teach Python specifically. Instead, the focus is on general programming concepts. As a result, several trade-offs are necessary and worth keeping in mind. Examples include:

- The use of `global` keywords for variable scope and explicit access to global variables. While this is generally discouraged, there is one case where it is necessary in order to progress before alternatives can be introduced.
- The use of patterns that may be considered 'un-Pythonic'. For example, this exercise uses manual getter and setter methods instead of direct attribute access or the `@property` decorator, which is encouraged to be used in Python. This approach supports the generalisation of object-oriented programming patterns that are relevant in other languages and contexts (e.g. Java or C++) while also helping to keep the learning units smaller, more focused, and more suitable for beginners.

In summary, the emphasis on smaller learning units and language-independent programming concepts makes certain trade-offs necessary.

## Contributions and improvements

This teaching project is open for contributions and improvements. Please contact me or use GitHub issues for discussion or pull-requests for improvements. Any contributions or comments are welcome!

## AI declaration

Generative AI has not been used in the conceptualisation or programming of this code.

## Contact

[Martin Sudmanns](https://www.plus.ac.at/geoinformatik/fachbereich/team/sudmanns/)  
University of Salzburg  
Department of Geoinformatics  
Schillerstraße 30  
5020 Salzburg  
Austria  
