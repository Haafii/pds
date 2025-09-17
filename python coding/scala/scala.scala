Scala list


1.// Scala program to print immutable lists
import scala.collection.immutable._

// Creating object
object GFG
{d((
Mpr
    // Main method
    def main(args:Array[String])
    {  
        // Creating and initializing immutable lists
        val mylist1: List[String] = List("Geeks", "GFG",
                            "GeeksforGeeks", "Geek123")
        val mylist2 = List("C", "C#", "Java", "Scala",
                                        "PHP", "Ruby")

        // Display the value of mylist1
        println("List 1:")
        println(mylist1)

        // Display the value of mylist2 using for loop
        println("\nList 2:")
        for(mylist<-mylist2)
        {
            println(mylist)
        }
    }
}

List 1:
List(Geeks, GFG, GeeksforGeeks, Geek123)

List 2:
C
C#
Java
Scala
PHP
Ruby


2.// Scala program to illustrate the
// use of empty list
import scala.collection.immutable._

// Creating object
object GFG
{
    // Main method
    def main(args: Array[String]): Unit =
    {
        // Creating an Empty List
        val emptylist: List[Nothing] = List()
        println("The empty list is:")
        println(emptylist)
    }
}
The empty list is:
List()



3.// Scala program to illustrate the 
// use of two dimensional list
import scala.collection.immutable._

// Creating object
object GFG
{
    // Main method
    def main(args: Array[String]): Unit =
    {
        // Creating a two-dimensional List
        val twodlist: List[List[Int]] =
          List(
            List(1, 0, 0),
            List(0, 1, 0),
            List(0, 0, 1)
          )

        println("The two dimensional list is:")
        println(twodlist)
    }
}

The two dimensional list is:
List(List(1, 0, 0), List(0, 1, 0), List(0, 0, 1))
4.// Scala program of a list to 
// perform head operation
import scala.collection.immutable._

// Creating object
object GFG
{
    // Main method
    def main(args: Array[String]): Unit =
    {
        // Creating a List
        val mylist = List("C", "C#", "Java", "Scala",
                          "PHP", "Ruby")

        println("The head of the list is:")
        println(mylist.head)
    }
}
5.// Scala program to perform
// tail operation of a list
import scala.collection.immutable._

// Creating object
object GFG
{
    // Main method
    def main(args: Array[String]): Unit =
    {
        // Creating a List
        val mylist = List("C", "C#", "Java", "Scala",
                          "PHP", "Ruby")

        println("The tail of the list is:")
        println(mylist.tail)
    }
}
6.// Scala program to perform
// isEmpty operation of a list
import scala.collection.immutable._

// Creating object
object GFG
{
    // Main method
    def main(args:Array[String])=Unit
    {
    
        // Creating a List.
        val mylist = List("C", "C#", "Java", "Scala",
                                     "PHP", "Ruby")
        println("List is empty or not:")
        println(mylist.isEmpty)
    }
}



7.// Scala program to creating a uniform list 
import scala.collection.immutable._

// Creating object
object GFG
{
    // Main method
    def main(args:Array[String])=Unit
    {
        // Repeats Scala three times.
        val programminglanguage = List.fill(3)("Scala") 
        println( "Programming Language : " + programminglanguage )

        // Repeats 2, 10 times.
        val number= List.fill(8)(4)         
        println("number : " + number)
    }
}


8.// Scala program of reversing a list order
import scala.collection.immutable._

// Creating object
object GFG
{
    // Main method
    def main(args:Array[String])=Unit
    {
        val mylist = List(1, 2, 3, 4, 5) 
        println("Original list:" + mylist)
        
        // reversing a list
        println("Reverse list:" + mylist.reverse)
    }
}


9.// Scala program to create a ListBuffer 
// ListBuffer class is imported 
import scala.collection.mutable.ListBuffer

// Creating object 
object GfG 
{ 
    // Main Method 
    def main(args: Array[String]): Unit = 
    { 
        // Instance of ListBuffer is created 
        var name = ListBuffer[String]()  

        name += "GeeksForGeeks"
        name += "gfg"
        name += "Class"

        println(name) 
    } 
}

10.// Scala program to add element in ListBuffer 
// ListBuffer class is imported 
import scala.collection.mutable.ListBuffer 

// Creating Object 
object GFG 
{ 
    // Main Method 
    def main(args: Array[String]): Unit = 
    { 
        // Instance of ListBuffer is created 
        var name = ListBuffer[String]() 
    
        // Adding one element 
        name += "GeeksForGeeks"
            
        // Add two or more elements 
        name += ("gfg", "class") 
        
        // Adding one or more elements using append method 
        name.append("Scala", "Article") 
            
        // Printing ListBuffer 
        println(name) 
    } 
}

11.// Scala program to delete element from ListBuffer 
// ListBuffer class is imported 
import scala.collection.mutable.ListBuffer 

// Creating Object 
object GFG 
{ 
    // Main Method 
    def main(args: Array[String]): Unit = 
    { 
        // Instance of ListBuffer is created 
        var name = ListBuffer("GeeksForGeeks", "gfg", 
                              "class", "Scala", 
                              "Article") 
    
        // Deletes one element 
        name -= "GeeksForGeeks"
            
        // Deletes two or more elements 
        name -= ("gfg", "class") 
        
        // Printing resultant ListBuffer 
        println(name) 
    } 
}


12.// Scala program for remove method on ListBuffer 
// ListBuffer class is imported 
import scala.collection.mutable.ListBuffer 

// Creating Object 
object GFG 
{ 
    // Main Method 
    def main(args: Array[String]): Unit = 
    { 
        // Instance of ListBuffer is created 
        var name = ListBuffer("GeeksForGeeks", 
                              "gfg", "class", 
                              "Scala", "Article") 
        
        // Removing 0th index element 
        name.remove(0) 
        
        // Printing resultant ListBuffer 
        println(name) 
        
        // Removing 3 elements starting from index 1
        name.remove(1, 3) 
        
        // Printing resultant ListBuffer 
        println(name) 
    } 
}



13.// Importing the mutable ListBuffer class from Scala collections
import scala.collection.mutable.ListBuffer

// Creating an object to hold our program
object ListBufferExample {

  // Main method: the entry point of the program
  def main(args: Array[String]): Unit = {
    
    // Create an empty ListBuffer of type Int (can grow/shrink dynamically)
    val listBuffer = ListBuffer[Int]()

    // Add single elements to the ListBuffer (+= adds one element at a time)
    listBuffer += 1
    listBuffer += 2
    listBuffer += 3
    // Now listBuffer = ListBuffer(1, 2, 3)

    // Append multiple elements from a sequence using ++=
    listBuffer ++= Seq(4, 5, 6)
    // Now listBuffer = ListBuffer(1, 2, 3, 4, 5, 6)

    // Insert an element at a specific index (index 2 gets the value 10)
    listBuffer.insert(2, 10)
    // Now listBuffer = ListBuffer(1, 2, 10, 3, 4, 5, 6)

    // Remove a specific element by value (removes the first "3")
    listBuffer -= 3
    // Now listBuffer = ListBuffer(1, 2, 10, 4, 5, 6)

    // Update an element at a specific index (index 1 changes from 2 to 20)
    listBuffer.update(1, 20)
    // Now listBuffer = ListBuffer(1, 20, 10, 4, 5, 6)

    // Convert the mutable ListBuffer to an immutable List
    val list = listBuffer.toList
    // list = List(1, 20, 10, 4, 5, 6)

    // Print both the mutable ListBuffer and the immutable List
    println("List buffer: " + listBuffer)
    println("List: " + list)
  }
}

14.object GroupAssignment1 {
  def main(args: Array[String]): Unit = {

    val nums: List[Int] = List(10, 20, 30, 40, 50)
    println(nums)  
    // Output: List(10, 20, 30, 40, 50)

    // print first element 
    println(s"FIRST ELEMENT: ${nums.head}")  
    // Output: FIRST ELEMENT: 10

    // print last element 
    println(s"LAST ELEMENT: ${nums.last}")  
    // Output: LAST ELEMENT: 50

    // print tail (all except first)
    println(s"TAIL: ${nums.tail}")  
    // Output: TAIL: List(20, 30, 40, 50)

    // check if list isEmpty
    println(s"LIST isEmpty? ${nums.isEmpty}")  
    // Output: LIST isEmpty? false

    // access element at an index
    println(s"Index 3 ELEMENT: ${nums.apply(3)}")  
    // Output: Index 3 ELEMENT: 40

    // add element to the beginning of the list
    val nums2 = 60 :: nums
    println(s"PREPEND: $nums2")  
    // Output: PREPEND: List(60, 10, 20, 30, 40, 50)

    // also possible using prepend
    val nums3 = 70 +: nums
    println(s"PREPEND: $nums3")  
    // Output: PREPEND: List(70, 10, 20, 30, 40, 50)

    // prepend a list 
    val nums4 = nums3 ++: nums2
    println(nums4)  
    // Output: List(70, 10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50)

    // append an element 
    val nums5 = nums :+ 55
    println(s"APPEND: $nums5")  
    // Output: APPEND: List(10, 20, 30, 40, 50, 55)

    // append a list
    val nums6 = nums5 :++ nums2
    println(nums6)  
    // Output: List(10, 20, 30, 40, 50, 55, 60, 10, 20, 30, 40, 50)

    // aggregate operations
    println(nums.min)   // Output: 10
    println(nums.max)   // Output: 50
    println(nums.sum)   // Output: 150
    println(nums.length)  // Output: 5
    println(nums.mkString)  // Output: 1020304050
    println(nums.mkString(","))  // Output: 10,20,30,40,50

    // list with mixed types
    val mixedList: List[Any] = List(1, "hello", 3.14, true, 'c')
    println(mixedList)  
    // Output: List(1, hello, 3.14, true, c)

    // Create a list of strings
    val fruits = List("apple", "banana", "mango", "orange", "grapes")
    println(s"ORIGINAL LISTS: $fruits")  
    // Output: ORIGINAL LISTS: List(apple, banana, mango, orange, grapes)

    // Basic operations
    println(s"HEAD: ${fruits.head}")  
    // Output: HEAD: apple
    println(s"TAIL: ${fruits.tail}")  
    // Output: TAIL: List(banana, mango, orange, grapes)
    println(s"IS EMPTY? ${fruits.isEmpty}")  
    // Output: IS EMPTY? false
    println(s"LENGTH: ${fruits.length}")  
    // Output: LENGTH: 5
    println(s"REVERSED: ${fruits.reverse}")  
    // Output: REVERSED: List(grapes, orange, mango, banana, apple)

    // Adding elements
    val prepend = “kiw

15.object ListExample {
  def main(args: Array[String]): Unit = {
      
    val listx = 2 :: 3 :: Nil   // Creates List(2, 3)
    val listy = 1 :: listx      // Prepends 1 → List(1, 2, 3)
    println(s"Listy is: ${listy}")  
    // Output: Listy is: List(1, 2, 3)

    println()

    val fillList = List.fill(10)(10)  
    // Creates a list with 10 elements, each being 10
    println(s"Fill list: ${fillList}")  
    // Output: Fill list: List(10, 10, 10, 10, 10, 10, 10, 10, 10, 10)

    println()

    val numbers = List(1,2,3,4,5,6,7,8,9,10)

    val num = List(3, 8, 1, 4, 2)
    val sortedNumbers = num.sorted  
    println(s"The sorted list is: ${sortedNumbers}")  
    // Output: The sorted list is: List(1, 2, 3, 4, 8)

    println()

    case class Person(name: String, age: Int)
    val people = List(Person("Alice",30), Person("Bob",25), Person("Charlie",35))
    val sortedPeople = people.sortBy(_.age)
    println(s"The sorted list based on the age is: ${sortedPeople}")  
    // Output: The sorted list based on the age is: List(Person(Bob,25), Person(Alice,30), Person(Charlie,35))

    println()

    println(s"First element: ${numbers.head}")  
    // Output: First element: 1

    println()
    println(s"Tail of the list: ${numbers.tail}")  
    // Output: Tail of the list: List(2, 3, 4, 5, 6, 7, 8, 9, 10)

    println()
    println(s"Element at index 2: ${numbers(2)}")  
    // Output: Element at index 2: 3

    println()
    val subList = numbers.slice(2, 6)
    println(s"Sublist from index 2 to 5: ${subList}")  
    // Output: Sublist from index 2 to 5: List(3, 4, 5, 6)

    println()
    val reverseList = numbers.reverse
    println(s"Reversed list: ${reverseList}")  
    // Output: Reversed list: List(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

    println()
    val list1 = List(1, 2, 3)
    val list2 = List(4, 5, 6)
    val combinedList = list1 ++ list2
    println(s"Combined list: ${combinedList}")  
    // Output: Combined list: List(1, 2, 3, 4, 5, 6)

    println()
    val listA = List(1, 2)
    val listB = List(3, 4)
    val listC = List(5, 6)
    val combined1List = listA ::: listB ::: listC
    println(s"Combined1 list: ${combined1List}")  
    // Output: Combined1 list: List(1, 2, 3, 4, 5, 6)

    println()
    val listOfLists = List(List(1, 2), List(3, 4), List(5, 6))
    val flattenedList = listOfLists.flatten
    println(s"Flattened list: ${flattenedList}")  
    // Output: Flattened list: List(1, 2, 3, 4, 5, 6)

    println()
    val multiplyNumbers = numbers.map(_ * 3)
    println(s"Multiplied numbers: ${multiplyNumbers}")  
    // Output: Multiplied numbers: List(3, 6, 9, 12, 15, 18, 21, 24, 27, 30)

    println()
    val evenNumbers = numbers.filter(_ % 2 == 0)
    println(s"Even numbers: ${evenNumbers}")  
    // Output: Even numbers: List(2, 4, 6, 8, 10)

    println()
    val sum = numbers.reduce(_ + _)
    println(s"Sum of numbers: ${sum}")  
    // Output: Sum of numbers: 55

    println()
    val foldedSum = numbers.foldLeft(0)(_ + _)
    println(s"Folded sum: ${foldedSum}")  
    // Output: Folded sum: 55

    println()
    val applyList = numbers.apply(3)
    println(s"The element at index 3 is: ${applyList}")  
    // Output: The element at index 3 is: 4

    println()
    val distinctNumbers = List(1,1,2,3,4,5,6,6,7,1)
    println(s"The list with distinct numbers: ${distinctNumbers.distinct}")  
    // Output: The list with distinct numbers: List(1, 2, 3, 4, 5, 6, 7)

    println()
    val foundElement = numbers.find(_ > 7)
    println(s"Find first element greater than 7: ${foundElement}")  
    // Output: Find first element greater than 7: Some(8)

    println()
    val firstFive = numbers.take(5)
    println(s"First five elements: ${firstFive}")  
    // Output: First five elements: List(1, 2, 3, 4, 5)

    println()
    val droppedFirstThree = numbers.drop(3)
    println(s"List after dropping first three: ${droppedFirstThree}")  
    // Output: List after dropping first three: List(4, 5, 6, 7, 8, 9, 10)

    println()
    val allPositive = numbers.forall(_ < 0)
    println(s"Are all numbers positive? ${allPositive}")  
    // Output: Are all numbers positive? false

    println()
    val hasEven = numbers.exists(_ % 2 == 0)
    println(s"Does the list have any even number? ${hasEven}")  
    // Output: Does the list have any even number? true

    println()
    println("Iterating through the list:")
    for(element <- numbers){
      println(element)
    }
    // Output:
    // Iterating through the list:
    // 1
    // 2
    // 3
    // 4
    // 5
    // 6
    // 7
    // 8
    // 9
    // 10

    println()
    println(s"Does the list contain 3? ${numbers.contains(3)}")  
    // Output: Does the list contain 3? true

    println()
    println(s"Size of the list: ${numbers.size}")  
    // Output: Size of the list: 10
  }
}

Array
1.// Scala 3 program to create an array of weekdays 
object GFG {

  // Main method
  def main(args: Array[String]): Unit = {

    // Creating and initializing a 1D Array of Strings
    val days = Array("Sunday", "Monday", "Tuesday", 
                     "Wednesday", "Thursday", "Friday", 
                     "Saturday")

    println("Array elements are:")

    // Iterating using for loop
    for (day <- days) {
      println(day)
    }
  }
}
Array elements are:
Sunday
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday

=== Code Execution Successful ===

2.// Scala program to access elements of an array
object GFG {

  // Main method
  def main(args: Array[String]): Unit = {

    // Creating and initializing a 1D Array of Strings
    val name = Array("gfg", "geeks", "GeeksQuize", "geeksforgeeks")

    println("Second element of the array is:")

    // Accessing an array element using index
    println(name(1))   // Index starts at 0, so name(1) = "geeks"
  }
}

3.// Scala program to update an array 
// of strings
object GFG {

  // Main method
  def main(args: Array[String]): Unit = {

    // Creating and initializing a 1D Array of Strings
    val name = Array("gfg", "geeks", "GeeksQuize", "geeksforgeeks")

    // Updating an element in the array (index 1 → "employee")
    name(1) = "employee"

    println("After updation, array elements are:")

    // Iterating through the array and printing elements
    for (m1 <- name) {
      println(m1)
    }
  }
}


3.// Scala program to add elements in an array
// of Strings
object GFG {

  // Main method
  def main(args: Array[String]): Unit = {

    // Creating an empty array of size 4
    val name = new Array 

    // Adding elements into the array (index-based assignment)
    name(0) = "gfg"
    name(1) = "geeks"
    name(2) = "GeeksQuize"
    name(3) = "geeksforgeeks"

    println("After adding array elements:")

    // Printing each element
    for (m1 <- name) {
      println(m1)
    }
  }
}

4.// Scala program to concatenate two arrays
// by using concat() method
import Array._

object GFG {

  // Main method
  def main(args: Array[String]): Unit = {

    // First array
    val arr1 = Array(1, 2, 3, 4)

    // Second array
    val arr2 = Array(5, 6, 7, 8)

    // Concatenating two arrays
    val arr3 = concat(arr1, arr2)

    // Print all elements of the new array
    for (x <- arr3) {
      println(x)
    }
  }
}
5.// Scala program to create a 
// multidimensional array of Strings, 
// store values in it, and print each value.
object GFG {
  // Main method
  def main(args: Array[String]): Unit = {
    val rows = 2
    val cols = 3

    // Declaring Multidimensional array
    val names = Array.ofDim[String](rows, cols)

    // Allocating values
    names(0)(0) = "gfg"
    names(0)(1) = "Geeks"
    names(0)(2) = "GeeksQuize"
    names(1)(0) = "GeeksForGeeks"
    names(1)(1) = "Employee"
    names(1)(2) = "Author"

    // Printing values
    for {
      i <- 0 until rows
      j <- 0 until cols
    } {
      println(s"($i)($j) = ${names(i)(j)}")
    }
  }
}
(0)(0) = gfg
(0)(1) = Geeks
(0)(2) = GeeksQuize
(1)(0) = GeeksForGeeks
(1)(1) = Employee
(1)(2) = Author
6.object GFG {

  // Main method
  def main(args: Array[String]): Unit = {

    // Declaring an array
    val a = Array(45, 52, 61) 
    println("Array a ")
    for (x <- a) {
      println(x)
    }
    // Output:
    // Array a 
    // 45
    // 52
    // 61

    // Appending 1 item
    val b = a :+ 27   // Adds 27 to the end of array 'a'
    println("Array b ")
    for (x <- b) {
      println(x)
    }
    // Output:
    // Array b 
    // 45
    // 52
    // 61
    // 27

    // Appending 2 items
    val c = b ++ Array(1, 2)   // Concatenates array [1, 2] at the end of 'b'
    println("Array c ")
    for (x <- c) {
      println(x)
    }
    // Output:
    // Array c 
    // 45
    // 52
    // 61
    // 27
    // 1
    // 2

    // Prepending 1 item
    val d = 3 +: c   // Adds 3 at the beginning of array 'c'
    println("Array d ")
    for (x <- d) {
      println(x)
    }
    // Output:
    // Array d 
    // 3
    // 45
    // 52
    // 61
    // 27
    // 1
    // 2

    // Prepending 2 items
    val e = Array(10, 25) ++: d   // Concatenates [10, 25] at the beginning of 'd'
    println("Array e ")
    for (x <- e) {
      println(x)
    }
    // Output:
    // Array e 
    // 10
    // 25
    // 3
    // 45
    // 52
    // 61
    // 27
    // 1
    // 2
  }
}

7.import Array._

object ABC {

  def main(args: Array[String]): Unit = {

    // ------------------------
    // One-dimensional arrays
    // ------------------------
    println("\nOne-dimensional arrays:")
    val names = Array("Samarth", "Parth", "Raj", "Yash", "Jay", "Dev", "Soham")
    println("Array elements are:")
    for (m <- names) println(m)
    // Output:
    // Samarth
    // Parth
    // Raj
    // Yash
    // Jay
    // Dev
    // Soham

    println(s"Single element name: ${names(0)}")
    // Output: Single element name: Samarth

    // ------------------------
    // Concatenating two arrays
    // ------------------------
    println("\nScala program to concatenate two arrays:")
    val arr1 = Array(1, 2, 3, 4, 57, 7, 89, 5, 9)
    val arr2 = Array(5, 6, 7, 8, 5, 7, 8, 9, 34, 6)
    val arr3 = concat(arr1, arr2)
    println(arr3.mkString(" "))
    // Output: 1 2 3 4 57 7 89 5 9 5 6 7 8 5 7 8 9 34 6

    // ------------------------
    // Array updation
    // ------------------------
    println("\nArray updation:")
    val nameUpd = Array("adithya", "parth", "Ashish", "samarth")
    println("Before updation: " + nameUpd.mkString(" "))
    // Output: Before updation: adithya parth Ashish samarth
    nameUpd(0) = "kishan"
    println("After updation: " + nameUpd.mkString(" "))
    // Output: After updation: kishan parth Ashish samarth

    // ------------------------
    // Adding elements to an array
    // ------------------------
    println("\nAdding elements in an array:")
    val nameArr = new Array 
    nameArr(0) = "Samarth"
    nameArr(1) = "Parth"
    nameArr(2) = "Adithya"
    nameArr(3) = "Ashish"
    println(nameArr.mkString(" "))
    // Output: Samarth Parth Adithya Ashish

    // ------------------------
    // Multidimensional arrays
    // ------------------------
    println("\nMultidimensional Arrays:")
    val rows = 2
    val cols = 3
    val names2D = Array.ofDim[String](rows, cols)
    names2D(0)(0) = "Samarth"
    names2D(0)(1) = "Parth"
    names2D(0)(2) = "Adithya"
    names2D(1)(0) = "Ashish"
    names2D(1)(1) = "Kishan"
    names2D(1)(2) = "MukundAnand"

    for (i <- 0 until rows; j <- 0 until cols) {
      println(s"($i)($j) = ${names2D(i)(j)}")
    }
    // Output:
    // (0)(0) = Samarth
    // (0)(1) = Parth
    // (0)(2) = Adithya
    // (1)(0) = Ashish
    // (1)(1) = Kishan
    // (1)(2) = MukundAnand

    // ------------------------
    // Transpose a matrix
    // ------------------------
    println("\nTranspose:")
    val matrix = Array(
      Array(1, 2, 3),
      Array(4, 5, 6),
      Array(7, 8, 9)
    )
    println("Original Matrix:")
    matrix.foreach(row => println(row.mkString(" ")))
    // Output:
    // 1 2 3
    // 4 5 6
    // 7 8 9

    val transpose = Array.ofDim[Int](matrix(0).length, matrix.length)
    for (i <- matrix.indices; j <- matrix(0).indices) {
      transpose(j)(i) = matrix(i)(j)
    }
    println("Transposed Matrix:")
    transpose.foreach(row => println(row.mkString(" ")))
    // Output:
    // 1 4 7
    // 2 5 8
    // 3 6 9

    // ------------------------
    // Append and Prepend elements
    // ------------------------
    println("\nAppend and Prepend elements:")
    val a = Array(45, 52, 61)
    println("Array a: " + a.mkString(" "))
    // Output: 45 52 61

    val b = a :+ 27
    println("Array b: " + b.mkString(" "))
    // Output: 45 52 61 27

    val c = b ++ Array(1, 2)
    println("Array c: " + c.mkString(" "))
    // Output: 45 52 61 27 1 2

    val d = 3 +: c
    println("Array d: " + d.mkString(" "))
    // Output: 3 45 52 61 27 1 2

    val e = Array(10, 25) ++: d
    println("Array e: " + e.mkString(" "))
    // Output: 10 25 3 45 52 61 27 1 2

    // ------------------------
    // Array operations
    // ------------------------
    println("\nArray operations:")
    val numbers = Array(1, 2, 3, 4, 5)
    println("Numbers: " + numbers.mkString(" "))
    // Output: 1 2 3 4 5

    val squares = Array.tabulate(5)(n => n * n)
    println("Squares: " + squares.mkString(" "))
    // Output: 0 1 4 9 16

    val evens = numbers.filter(_ % 2 == 0)
    println("Even numbers: " + evens.mkString(" "))
    // Output: 2 4

    val words = Array("hello", "world")
    val allChars = words.flatMap(_.toUpperCase)
    println("FlatMap (all characters): " + allChars.mkString(" "))
    // Output: H E L L O W O R L D

    val nums = Array(1, 2, 3, 4)
    val sum = nums.reduce(_ + _)
    println("Sum of given array: " + sum)
    // Output: 10
  }
}

Array Buffer

1.// Scala 3 program to create an ArrayBuffer
import scala.collection.mutable.ArrayBuffer

object GFG {

  def main(args: Array[String]): Unit = {
    // Create an empty ArrayBuffer of Strings
    var name = ArrayBuffer[String]()

    // Add elements
    name += "GeeksForGeeks"
    name += "gfg"
    name += "Chandan"

    // Print ArrayBuffer
    println(name)
  }
}
2.// Scala 3 program to access element of ArrayBuffer
import scala.collection.mutable.ArrayBuffer

object GFG {

  def main(args: Array[String]): Unit = {
    // Create an empty ArrayBuffer of Strings
    var name = ArrayBuffer[String]()

    // Add elements
    name += "GeeksForGeeks"
    name += "gfg"
    name += "Chandan"

    // Accessing 1st index element (second element)
    println(name(1))
  }
}
3.// Scala program to add element in ArrayBuffer
// ArrayBuffer class is imported
import scala.collection.mutable.ArrayBuffer

// Creating Object
object GFG
{
    
// Main Method
def main(args: Array[String]) 
{
    // Instance of ArrayBuffer is created
    var name = ArrayBuffer[String]() 

    // adding one element
    name += "GeeksForGeeks"
        
    // add two or more elements 
    name += ("gfg", "chandan")
        
    // adding one or more element using append method 
    name.append("S-series", "Ritesh") 
    
    // printing arraybuffer
    println(name) 
}
}4.// Scala program to delete element from ArrayBuffer
// ArrayBuffer class is imported
import scala.collection.mutable.ArrayBuffer

// Creating Object
object GFG 
{
    
// Main Method
def main(args: Array[String]) 
{
    // Instance of ArrayBuffer is created
    var name = ArrayBuffer( "GeeksForGeeks","gfg",
                            "chandan","S-series", 
                            "Ritesh" ) 

    // deletes one element
    name -= "GeeksForGeeks"
        
    // deletes two or more elements 
    name -= ("gfg", "chandan")
    
    // printing resultant arraybuffer
    println(name) 
}
}5.// Scala program for remove method, on ArrayBuffer
// ArrayBuffer class is imported
import scala.collection.mutable.ArrayBuffer

// Creating Object
object GFG 
{
    
// Main Method
def main(args: Array[String]) 
{
    // Instance of ArrayBuffer is created
    var name = ArrayBuffer( "GeeksForGeeks",
                            "gfg", "chandan",
                            "S-series", "Ritesh" ) 
    
    // removing 0th index element
    name.remove(0) 
    
    // printing resultant arraybuffer
    println(name)
    name.remove(1, 3)
    
    // printing resultant arraybuffer
    println(name) 
}
}
6.import scala.collection.mutable.ArrayBuffer

object LabExercise {
  def main(args: Array[String]): Unit = {

    println("Creating an ArrayBuffer")
    val numbers = ArrayBuffer[Int](60, 20, 30, 40, 10)
    println(s"List of elements in arraybuffer: $numbers")
    // Output: ArrayBuffer(60, 20, 30, 40, 10)

    numbers += 70
    println(s"ArrayBuffer after adding 70 in the last: $numbers")
    // Output: ArrayBuffer(60, 20, 30, 40, 10, 70)

    println("\nAccessing elements")
    println(s"Element at index 0: ${numbers(0)}")
    // Output: Element at index 0: 60
    println(s"Element at index 3: ${numbers(3)}")
    // Output: Element at index 3: 40

    println("\nUpdating an element")
    numbers(1) = 25
    println(s"ArrayBuffer after updating element at index 1: $numbers")
    // Output: ArrayBuffer(60, 25, 30, 40, 10, 70)

    println("\nRemoving an element")
    numbers -= 40
    println(s"ArrayBuffer after removing the value 40: $numbers")
    // Output: ArrayBuffer(60, 25, 30, 10, 70)

    numbers.remove(1)
    println(s"ArrayBuffer after removing element at index 1: $numbers")
    // Output: ArrayBuffer(60, 30, 10, 70)

    println("\nPrepending elements")
    val prepend1 = 5 +: numbers
    println(s"After prepending 5: $prepend1")
    // Output: ArrayBuffer(5, 60, 30, 10, 70)

    val prepend2 = ArrayBuffer(1, 2) ++: numbers
    println(s"After prepending ArrayBuffer(1,2): $prepend2")
    // Output: ArrayBuffer(1, 2, 60, 30, 10, 70)

    println("\nIterating through the elements")
    for (element <- numbers) {
      print(s"$element ")
    }
    println()
    // Output: 60 30 10 70 

    println("\nSorting the elements")
    val sortedNumbers = numbers.sortBy(identity)
    println(sortedNumbers)
    // Output: ArrayBuffer(10, 30, 60, 70)
  }
}




Set
1.// Scala 3 program to illustrate immutable set
import scala.collection.immutable.*

object Main {
  def main(args: Array[String]): Unit = {

    // Creating and initializing immutable sets
    val myset1: Set[String] = Set("Geeks", "GFG", "GeeksforGeeks", "Geek123")
    val myset2 = Set("C", "C#", "Java", "Scala", "PHP", "Ruby")

    // Display the value of myset1
    println("Set 1:")
    println(myset1)

    // Display the value of myset2 using for loop
    println("\nSet 2:")
    for (myset <- myset2) {
      println(myset)
    }
  }
}
2.// Scala 3 program to illustrate the use of mutable set
import scala.collection.mutable.Set

object Main {
  def main(args: Array[String]): Unit = {

    // Creating and initializing mutable sets
    var myset1: Set[String] = Set("Geeks", "GFG", "GeeksforGeeks", "Geek123")
    var myset2: Set[Int] = Set(10, 100, 1000, 10000, 100000)

    // Display the value of myset1
    println("Set 1:")
    println(myset1)

    // Modifying the mutable set (adding/removing)
    myset1 += "NewElement"
    myset1 -= "GFG"
    println(s"Updated Set 1: $myset1")

    // Display the value of myset2 using foreach
    println("\nSet 2:")
    myset2.foreach((item: Int) => println(item))

    // Adding a new element to myset2
    myset2 += 500
    println(s"Updated Set 2: $myset2")
  }
}
3.// Scala 3 program to get sorted values from the set
import scala.collection.immutable.SortedSet

object Main {
  def main(args: Array[String]): Unit = {

    // Using SortedSet to get sorted values
    val myset: SortedSet[Int] = SortedSet(87, 0, 3, 45, 7, 56, 8, 6)

    println("Sorted Set elements are:")
    myset.foreach((items: Int) => println(items))
  }
}
4.set Mutable
// Scala 3 program to illustrate how to  
// add items using +=, ++= and add() 
// method in mutable set

import scala.collection.mutable._

object Main {
  def main(args: Array[String]): Unit = {

    // Creating and initializing set
    var myset = Set("G", "Geek", "for")

    println(s"Initial Set: $myset")

    // Adding new element in set using +=
    myset += "Geeks"
    println(s"After adding 'Geeks' using += : $myset")

    // Adding multiple elements using ++=
    // "G" already exists, so it will not be added again
    myset ++= List("Geeks12", "geek23", "G")
    println(s"After adding List(Geeks12, geek23, G) using ++= : $myset")

    // Adding elements using add() method
    myset.add("GeeksforGeeks")
    println(s"After adding 'GeeksforGeeks' using add(): $myset")

    myset.add("geeksForgeeks100")
    println(s"After adding 'geeksForgeeks100' using add(): $myset")

    println(s"\nFinal Set: $myset")
  }
}
Initial Set: HashSet(G, Geek, for)
After adding 'Geeks' using += : HashSet(Geek, Geeks, for, G)
After adding List(Geeks12, geek23, G) using ++= : HashSet(Geek, Geeks12, Geeks, for, G, geek23)
After adding 'GeeksforGeeks' using add(): HashSet(Geek, Geeks12, Geeks, for, G, GeeksforGeeks, geek23)
After adding 'geeksForgeeks100' using add(): HashSet(Geek, Geeks12, Geeks, for, G, GeeksforGeeks, geek23, geeksForgeeks100)

Final Set: HashSet(Geek, Geeks12, Geeks, for, G, GeeksforGeeks, geek23, geeksForgeeks100)
5.// Scala program to illustrate
// how to delete items using -= 
// and --= methods in mutable set 
// with mutable collection
import scala.collection.mutable._

object Main 
{
    def main(args: Array[String]) 
    {
        
        // Creating and initializing 
        //mutable set
        var myset = Set(100, 400, 500, 
                        600, 300, 800)
        println(&quot;Set before deletion:&quot;)
        println(myset)
        
        // Deleting elements in set 
        // using -= and --= methods
        myset -= 600
        myset --= List(300, 100)
        println(&quot;\nSet after deletion:&quot;)
        println(myset)
    
    }
}
Initial Set: HashSet(100, 400, 500, 600, 300, 800)
After removing 600 using -= : HashSet(100, 400, 500, 300, 800)
After removing List(300, 100) using --= : HashSet(400, 500, 800)

Final Set: HashSet(400, 500, 800)
6.// Scala program to illustrate 
// how to delete items using 
// retain(), and clear() methods
import scala.collection.mutable._

object Main {
  def main(args: Array[String]): Unit = {

    // Creating and initializing mutable sets
    var myset1 = Set(100, 400, 500, 600, 300, 800)
    var myset2 = Set(11, 44, 55, 66, 77)

    println(s"Set 1 before deletion: $myset1")
    println(s"Set 2 before deletion: $myset2")

    // Deleting elements in set using retain() method
    // Retain elements greater than 500
    myset1.retain(_ > 500)
    println(s"\nSet 1 after using retain(_ > 500) method: $myset1")

    // Deleting elements in set using clear() method
    myset2.clear()
    println(s"\nSet 2 after using clear() method: $myset2")
  }
}
7// Scala program to illustrate how 
// to add elements in immutable set
import scala.collection.immutable._

object Main {
  def main(args: Array[String]): Unit = {

    // Creating and initializing immutable sets
    val myset1 = Set(100, 400, 500, 600, 300, 800)
    val myset2 = Set(11, 44, 55, 66, 77)

    println(s"Set 1 before addition: $myset1")
    println(s"Set 2 before addition: $myset2")
    println("\nSet after addition:")

    // Add single element in myset1 and create new Set
    val S1 = myset1 + 900
    println(s"After adding single element 900: $S1")

    // Add multiple elements in myset1 and create new Set
    val S2 = myset1 + (200, 300)
    println(s"After adding multiple elements 200, 300: $S2")

    // Add another list into myset1 and create new Set
    val S3 = myset1 ++ List(700, 1000)
    println(s"After adding List(700, 1000): $S3")

    // Add another set myset2 into myset1 and create new Set
    val S4 = myset1 ++ myset2
    println(s"After adding Set 2 into Set 1: $S4")
  }
}
8// Scala program to illustrate how 
// to remove elements in immutable set
import scala.collection.immutable._

object Main 
{
    def main(args: Array[String]) 
    {
        
        // Creating and initializing
        // immutable set
        val myset = Set(100, 400, 500, 600, 
                        300, 800, 900, 700)
        println(&quot;Set before deletion:&quot;)
        println(myset)
    
        println(&quot;\nSet after deletion:&quot;)
        
        // Remove single element in myset and 
        // Result store into new variable
        val S1 = myset - 100
        println(S1)
        
        // Remove multiple elements from myset 
        // Result store into new variable
        val S2 = myset - (400, 300)
        println(S2)
        
        // Remove another list from myset
        // Result store into new variable
        val S3 = myset -- List(700, 500)
        println(S3)
    }

}

9// Scala program to illustrate union, 
// intersection, and difference on Set 
import scala.collection.immutable._

object Main {
  def main(args: Array[String]): Unit = {

    // Creating and initializing sets
    val myset1 = Set(11, 22, 33, 44, 55, 66, 77, 111)
    val myset2 = Set(88, 22, 99, 44, 55, 66, 77)

    // Intersection
    val S1 = myset1.intersect(myset2)
    println(s"Intersection of Set1 and Set2: $S1")

    // Difference (Set1 - Set2)
    val S2 = myset1.diff(myset2)
    println(s"Difference of Set1 and Set2 (Set1 - Set2): $S2")

    // Union
    val S3 = myset1.union(myset2)
    println(s"Union of Set1 and Set2: $S3")
  }
}
10.object CollegeSetDemo {
  def main(args: Array[String]): Unit = {

    // Initial sets
    val mathStudents: Set[String] = Set("Ushodaya", "Sandeep", "Gaurav", "Ruszzikesh")
    val scienceStudents: Set[String] = Set("Ushodaya", "Gaurav", "Amar", "Sanjay")
    val englishStudents: Set[String] = Set("Ushodaya", "Sandeep", "Vishwa", "Ganesh")

    println("Math Students: " + mathStudents) 
    // Output: Math Students: Set(Ushodaya, Sandeep, Gaurav, Ruszzikesh)

    println("Science Students: " + scienceStudents) 
    // Output: Science Students: Set(Ushodaya, Gaurav, Amar, Sanjay)

    println("English Students: " + englishStudents) 
    // Output: English Students: Set(Ushodaya, Sandeep, Vishwa, Ganesh)

    // === Union ===
    val allStudents = mathStudents union scienceStudents union englishStudents
    println("\nAll Students (Union): " + allStudents)
    // Output: All Students (Union): Set(Ushodaya, Sandeep, Gaurav, Ruszzikesh, Amar, Sanjay, Vishwa, Ganesh)

    // === Intersection ===
    val commonStudents = mathStudents intersect scienceStudents intersect englishStudents
    println("All Common Students: " + commonStudents)
    // Output: All Common Students: Set(Ushodaya)

    // === Difference ===
    val onlyMath = mathStudents diff (scienceStudents union englishStudents)
    println("Only Math Students: " + onlyMath)
    // Output: Only Math Students: Set(Ruszzikesh)

    // === Extra Set Operations ===
    println("\n--- Extra Set Operations ---")

    // isEmpty
    println("Is Math Set Empty? " + mathStudents.isEmpty)
    // Output: Is Math Set Empty? false

    // size
    println("Number of Math Students: " + mathStudents.size)
    // Output: Number of Math Students: 4

    // head and tail
    println("First Student in Math Set (head): " + mathStudents.head)
    // Output (example, may vary due to set ordering): First Student in Math Set (head): Ushodaya
    println("All except first (tail): " + mathStudents.tail)
    // Output (example): All except first (tail): Set(Sandeep, Gaurav, Ruszzikesh)

    // contains
    println("Does Math Set contain 'Sandeep'? " + mathStudents.contains("Sandeep"))
    // Output: Does Math Set contain 'Sandeep'? true

    // subsetOf
    println("Is Math Set a subset of All Students? " + mathStudents.subsetOf(allStudents))
    // Output: Is Math Set a subset of All Students? true

    // map (transform each element)
    val upperCaseStudents = mathStudents.map(_.toUpperCase)
    println("Math Students in Uppercase: " + upperCaseStudents)
    // Output: Math Students in Uppercase: Set(USHODAYA, SANDEEP, GAURAV, RUSZZIKESH)

    // filter
    val namesWithS = allStudents.filter(_.startsWith("S"))
    println("Students whose name starts with 'S': " + namesWithS)
    // Output: Students whose name starts with 'S': Set(Sandeep, Sanjay)

    // forall (check condition for all elements)
    println("Do all Science Students have names longer than 3 letters? " + scienceStudents.forall(_.length > 3))
    // Output: Do all Science Students have names longer than 3 letters? true

    // exists (check if any element matches condition)
    println("Does any English Student's name start with V? " + englishStudents.exists(_.startsWith("V")))
    // Output: Does any English Student's name start with V? true

    // min and max (lexicographically)
    println("Alphabetically first student in Math: " + mathStudents.min)
    // Output: Alphabetically first student in Math: Gaurav
    println("Alphabetically last student in Math: " + mathStudents.max)
    // Output: Alphabetically last student in Math: Ushodaya

    // === Adding and Removing Elements ===
    val updatedMath = mathStudents + "Ganesh" - "Sandeep"
    println("Math Students after Adding Ganesh and Removing Sandeep: " + updatedMath)
    // Output: Math Students after Adding Ganesh and Removing Sandeep: Set(Ushodaya, Gaurav, Ruszzikesh, Ganesh)

    // ++ (adding multiple elements)
    val extendedMath = mathStudents ++ Set("Anjali", "Deepak")
    println("Math Students after adding multiple students: " + extendedMath)
    // Output: Math Students after adding multiple students: Set(Ushodaya, Sandeep, Gaurav, Ruszzikesh, Anjali, Deepak)

    // -- (removing multiple elements)
    val reducedMath = extendedMath -- Set("Ushodaya", "Deepak")
    println("Math Students after removing multiple students: " + reducedMath)
    // Output: Math Students after removing multiple students: Set(Sandeep, Gaurav, Ruszzikesh, Anjali)

  }
}




TUPLE
// Scala 3 program to access elements of a Tuple

object GFG:
  def main(args: Array[String]) =
    // Creating a tuple with 3 elements
    val name = (15, "chandan", true)

    // Accessing elements using _1, _2, _3
    println(name._1)   // Output: 15
    println(name._2)   // Output: chandan
    println(name._3)   // Output: true
2.// Scala 3 program of pattern matching on tuples

object GFG:
  def main(args: Array[String]) =
    // Pattern matching: deconstruct the tuple into variables a, b, c
    val (a, b, c) = (15, "chandan", true)

    println(a)   // Output: 15
    println(b)   // Output: chandan
    println(c)   // Output: true
3.// Scala 3 program to iterate over tuples
// using productIterator method

object GFG:
  def main(args: Array[String]) =
    val name = (15, "chandan", true)
    
    // Iterate over tuple elements using productIterator
    name.productIterator.foreach { i =>
      println(i)
    }
4.// Scala 3 program to swap tuple elements

object GFG:
  def main(args: Array[String]) =
    val name = ("geeksforgeeks", "gfg")
    
    // Swap tuple elements and print
    println(name.swap)
5.object TupleExample {
  def main(args: Array[String]): Unit = {
    // Creating two tuples
    val tuple1 = (1, "hello", 3.14)    // Tuple3[Int, String, Double]
    val tuple2 = ("world", 42)          // Tuple2[String, Int]

    // Print entire tuples
    println(tuple1)  // Output: (1,hello,3.14)
    println(tuple2)  // Output: (world,42)

    // Accessing elements using _n
    println(tuple1._2)  // Output: hello  (2nd element of tuple1)
    println(tuple2._1)  // Output: world  (1st element of tuple2)
  }
}



Vectors

object VectorOperations {
  def main(args: Array[String]): Unit = {
    // Create a Vector
    val vec = Vector(10, 20, 30, 40)

    // Access elements
    println(s"First element: ${vec.head}")        // 10
    println(s"Last element: ${vec.last}")         // 40
    println(s"Element at index 2: ${vec(2)}")     // 30

    // Add elements
    val appended = vec :+ 50
    val prepended = 5 +: vec
    println(s"Appended: $appended")               // Vector(10, 20, 30, 40, 50)
    println(s"Prepended: $prepended")             // Vector(5, 10, 20, 30, 40)

    // Concatenate vectors
    val combined = vec ++ Vector(60, 70)
    println(s"Combined: $combined")               // Vector(10, 20, 30, 40, 60, 70)

    // Update element
    val updated = vec.updated(1, 25)
    println(s"Updated index 1: $updated")         // Vector(10, 25, 30, 40)

    // Slice and take
    println(s"Slice (1 to 3): ${vec.slice(1, 4)}") // Vector(20, 30, 40)
    println(s"Take first 2: ${vec.take(2)}")       // Vector(10, 20)
    println(s"Drop first 2: ${vec.drop(2)}")       // Vector(30, 40)

    // Reverse and sort
    println(s"Reversed: ${vec.reverse}")           // Vector(40, 30, 20, 10)
    println(s"Sorted: ${vec.sorted}")              // Vector(10, 20, 30, 40)

    // Map and filter
    println(s"Doubled: ${vec.map(_ * 2)}")         // Vector(20, 40, 60, 80)
    println(s"Filtered (>25): ${vec.filter(_ > 25)}") // Vector(30, 40)

    // Check properties
    println(s"Contains 30? ${vec.contains(30)}")   // true
    println(s"Is empty? ${vec.isEmpty}")           // false
    println(s"Length: ${vec.length}")              // 4

    // Heterogeneous vectors
    val vec1: Vector[Any] = Vector(1, "s", "k", 5.5)
    println(s"vec1: $vec1")                        // Vector(1, s, k, 5.5)

    val vec2 = (1, "ssss", "kkk", 5.5)             // Tuple4
    println(s"vec2: $vec2")                        // (1,ssss,kkk,5.5)

    // ERROR FIX: vec3 must be created with Vector, not []
    val vec3: Vector[Any] = Vector(1, 2.5, "sss")
    println(s"vec3: $vec3")                        // Vector(1, 2.5, sss)

    val data: Seq[Any] = Vector(1, 2.5, "sasi")
    println(s"data: $data")                        // Vector(1, 2.5, sasi)
  }
}


Hashmap
// Immutable Map
val imMap = scala.collection.immutable.Map("Ajay" -> 30, "Bhavesh" -> 20)

// Mutable Map
val muMap = scala.collection.mutable.Map("Ajay" -> 30, "Bhavesh" -> 20)

// Access
val age = imMap("Ajay") // 30
val safeAge = imMap.getOrElse("John", 0) // 0 (default)

// Update immutable map (creates a NEW map)
val updatedMap = imMap + ("Ajay" -> 35) // Ajay updated

// Update mutable map (in-place)
muMap("Ajay") = 35

// Remove from immutable map (creates new map)
val reducedMap = imMap - "Bhavesh"

// Remove from mutable map (in-place)
muMap -= "Bhavesh"



1.object StudentScoresDemo {
  def main(args: Array[String]): Unit = {
    // Immutable Map of students with scores
    val studentScores = Map("Alice" -> 85, "Bob" -> 92, "Charlie" -> 78)

    // Filtering students who scored > 80
    val topScorers = studentScores.filter { case (_, score) => score > 80 }

    // Printing results
    println("All Student Scores: " + studentScores)
    println("Students scored > 80: " + topScorers)
  }
}

2.object HelloWorld {
  def main(args: Array[String]): Unit = {

    // Flight details with delays (in hours)
    val flightDelays = Map(
      "FL101" -> 3.5,
      "FL102" -> 1.0,
      "FL103" -> 0.5,
      "FL104" -> 2.5,
      "FL105" -> 0.0
    )

    val ticketPrice = 1000 // Assume fixed ticket price

    // Calculate refunds
    val refunds = flightDelays.map {
      case (flightNo, delay) if delay >= 3 =>
        (flightNo, s"Delay: $delay hr → Full Refund: ₹$ticketPrice")
      case (flightNo, delay) if delay >= 1 =>
        (flightNo, s"Delay: $delay hr → Half Refund: ₹${ticketPrice / 2}")
      case (flightNo, delay) =>
        (flightNo, s"Delay: $delay hr → No Refund")
    }

    // Print refund status for each flight
    println("=== Flight Refund Status ===")
    refunds.foreach { case (flightNo, status) =>
      println(s"$flightNo -> $status")
    }
  }
}

3.object StudentMarks {
  def main(args: Array[String]): Unit = {

    // Creating a map of regno -> marks
    val studentScores = Map(
      "R101" -> 12,
      "R102" -> 25,
      "R103" -> 8,
      "R104" -> 18,
      "R105" -> 14
    )

    println("Original Student Scores:")
    println(studentScores)

    // Increase 5 marks for students who scored < 15
    val updatedScores = studentScores.map {
      case (regno, mark) if mark < 15 => (regno, mark + 5)
      case (regno, mark)              => (regno, mark)
    }

    println("\nUpdated Student Scores (after +5 for <15):")
    println(updatedScores)
  }
}

1.
object StudenAttendence{
    def main(args:Array[String]):Unit={
        val attendence=Map("R101" -> 80, "R102" -> 65, "R103" -> 90, "R104" -> 70, "R105" -> 88)
        val defualters= attendence.filter{
            case (_,percentage)=>percentage<75
        }
        print(defualters)

    }
}

2.import scala.collection.mutable.Map

object EVFleetManager {
  def main(args: Array[String]): Unit = {
    
   
    val evBatteries: Map[String, Int] = Map(
      "EV101" -> 15,
      "EV102" -> 80,
      "EV103" -> 50,
      "EV104" -> 10,
      "EV105" -> 90
    )

    println("Initial battery levels:")
    println(evBatteries)
    
    evBatteries.foreach{
        case (id,battery)=>if battery<20 then println(id)
    }
    evBatteries("EV104")=60
    println(evBatteries)
    
    evBatteries -= "EV103"
     println(evBatteries)
    
  }
}
3.// Online Scala Editor for free
// Write, Edit and Run your Scala code using Scala Online Compiler

object HealthInsuranceAnalysis {
  def main(args: Array[String]): Unit = {

    val claims: List[Int] = List(
      120000, 80000, 150000, 95000, 50000,
      200000, 110000, 70000, 130000, 85000,
      90000, 175000, 40000, 160000, 125000,
      95000, 105000, 60000, 140000, 100000
    )

    val reasons: List[String] = List(
      "Surgery", "Fever", "Accident", "Checkup", "Infection",
      "Cardiology", "Orthopedic", "Fever", "Surgery", "Checkup",
      "Infection", "Accident", "Dental", "Cardiology", "Orthopedic",
      "Fever", "Surgery", "Dental", "Accident", "Checkup"
    )


    println("Claims above 1,00,000:")
    for ((claim, reason) <- claims.zip(reasons)) {
      if claim > 100000 then
        println(s"Claim: $claim, Reason: $reason")
    }

    
    var total: Double = 0
    var index: Int = 0
    while index < claims.length do
      total += claims(index)
      index += 1
    println(f"\nTotal Claim Amount: $total%.2f")
    
    val claimsWithFee: List[Double] = for (c <- claims) yield c * 1.10
    println("\nClaims with 10% processing fee added:")
    println(claimsWithFee.map(c => f"$c%.2f"))
    
    val clustered = for ((claim, reason) <- claims.zip(reasons)) yield {
      val level = if claim < 75000 then "Small"
                  else if claim <= 150000 then "Medium"
                  else "High"
      (claim, reason, level)
    }

    println("\nClustered Claim Data (Claim, Reason, Level):")
    clustered.foreach(println)


  }
}
