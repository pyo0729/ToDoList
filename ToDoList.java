import java.util.Scanner;

public class ToDoList
{
   public static void main (String arg[])
   {
   Scanner keyboard = new Scanner(System.in);
      
      ToDo List = new ToDo();
      
      List.makeList();
      
      boolean quit = false;
      
      do
      {
         System.out.println("1. View List" + "\n2. Add Task" + "\n3. Remove Task" + "\n4. Quit");
         int num = keyboard.nextInt();
         
         if(num > 4)
            System.out.println("That is not an option. Choose another!");
         else if(num == 1)
            List.viewList();
         else if(num == 2)
         {
            keyboard.nextLine();
            
            System.out.println("Enter task to add:");
            String task = keyboard.nextLine();
            
            List.addTask(task);
            
            System.out.println("Task entered successfully!");
         }
         else if(num == 3)
         {
            keyboard.nextLine();
            
            System.out.println("Enter task to remove:");
            String task = keyboard.nextLine();
            
            List.removeTask(task);
            
            System.out.println("Task removes successfully!");
         }
         else if(num == 4)
         {
            quit = true;
            System.out.println("Exiting list");
         }
         
         
      } while (!quit);
      
   }
}