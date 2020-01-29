object hello{
  def main(args: Array[String]): Unit={
    println("hello, Scala!")
    
    val name = "David"
    
    println(s"hello! ${name}")

    val height:Double=182.3
    println(f"$name%s is $height%2.2f meters tall")
    Arrays.asList(1,2,3).stream().reduce((a,b)-> a-b).get();
  }
}

