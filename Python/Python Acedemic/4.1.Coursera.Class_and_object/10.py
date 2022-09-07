# You have already seen that each instance of a class has its own namespace with its own instance variables. Two instances of the Point class each have their own instance variable x. Setting x in one instance doesn’t affect the other instance.

# A class can also have class variables. A class variable is set as part of the class definition.

# For example, consider the following version of the Point class. Here we have added a graph method that generates a string representing a little text-based graph with the Point plotted on the graph. It’s not a very pretty graph, in part because the y-axis is stretched like a rubber band, but you can get the idea from this.

# Note that there is an assignment to the variable printed_rep on line 4. It is not inside any method. That makes it a class variable. It is accessed in the same way as instance variables. For example, on line 16, there is a reference to self.printed_rep. If you change line 4, you have it print a different character at the x,y coordinates of the Point in the graph.









class Point:

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) +2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())











# To be able to reason about class variables and instance variables, it is helpful to know the rules that the python interpreter uses. That way, you can mentally simulate what the interpreter does.

# When the interpreter sees an expression of the form <obj>.<varname>, it:
# Checks if the object has an instance variable set. If so, it uses that value.

# If it doesn’t find an instance variable, it checks whether the class has a class variable. If so it uses that value.

# If it doesn’t find an instance or a class variable, it creates a runtime error (actually, it does one other check first, which you will learn about in the next chapter).

# When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
# Evaluates the expression on the right-hand side to yield some python object;

# Sets the instance variable <varname> of <obj> to be bound to that python object. Note that an assignment statement of this form never sets the class variable; it only sets the instance variable.

# In order to set the class variable, you use an assignment statement of the form <varname> = <expr> at the top-level in a class definition, like on line 4 in the code above to set the class variable printed_rep.

# In case you are curious, method definitions also create class variables. Thus, in the code above, graph becomes a class variable that is bound to a function/method object. p1.graph() is evaluated by:
# looking up p1 and finding that it’s an instance of Point

# looking for an instance variable called graph in p1, but not finding one

# looking for a class variable called graph in p1’s class, the Point class; it finds a function/method object

# Because of the () after the word graph, it invokes the function/method object, with the parameter self bound to the object p1 points to.

# Try running it in codelens and see if you can follow how it all works.

















# Thinking About Classes and Instances
# You can now imagine some reasons you may want to define a class. You have seen examples of creating types that are more complicated or specific than the ones built in to Python (like lists or strings). Turtle, with all the instance variables and methods you learned about using earlier in the semester, is a class that programmers defined which is now included in the Python language. In this chapter, we defined Point with some functionality that can make it easier to write programs that involve x,y coordinate Point instances. And shortly, you’ll see how you can define classes to represent objects in a game.

# You can also use self-defined classes to hold data – for example, data you get from making a request to a REST API.

# Before you decide to define a new class, there are a few things to keep in mind, and questions you should ask yourself:

# What is the data that you want to deal with? (Data about a bunch of songs from iTunes? Data about a bunch of tweets from Twitter? Data about a bunch of hashtag searches on Twitter? Two numbers that represent coordinates of a point on a 2-dimensional plane?)

# What will one instance of your class represent? In other words, which sort of new thing in your program should have fancy functionality? One song? One hashtag? One tweet? One point? The answer to this question should help you decide what to call the class you define.

# What information should each instance have as instance variables? This is related to what an instance represents. See if you can make it into a sentence. “Each instance represents one < song > and each < song > has an < artist > and a < title > as instance variables.” Or, “Each instance represents a < Tweet > and each < Tweet > has a < user (who posted it) > and < a message content string > as instance variables.”

# What instance methods should each instance have? What should each instance be able to do? To continue using the same examples: Maybe each song has a method that uses a lyrics API to get a long string of its lyrics. Maybe each song has a method that returns a string of its artist’s name. Or for a tweet, maybe each tweet has a method that returns the length of the tweet’s message. (Go wild!)

# What should the printed version of an instance look like? (This question will help you determine how to write the __str__ method.) Maybe, “Each song printed out will show the song title and the artist’s name.” or “Each Tweet printed out will show the username of the person who posted it and the message content of the tweet.”

# After considering those questions and making decisions about how you’re going to get started with a class definition, you can begin to define your class.

# Remember that a class definition, like a function definition, is a general description of what every instance of the class should have. (Every Point has an x and a y.) The class instances are specific: e.g. the Point with a specific x and y >. You might have a Point with an x value of 3 and a y value of 2, so for that particular instance of the class Point, you’d pass in 3 and 2 to the constructor, the __init__ method, like so: new_point = Point(3,2), as you saw in the last sections.

# You have attempted 1 of 1 activities on this page