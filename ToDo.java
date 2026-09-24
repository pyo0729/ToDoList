import java.util.ArrayList;

public class ToDo
{
   public ArrayList<String> List;
   public String Task;
   int num = 0;
   
   public void makeList()
   {
      List = new ArrayList<>();
   }
   
   public void Task(String t)
   {
      Task = t;
   }
   
   public void addTask(String task)
   {
      List.add(task);
      num++;
   }
   
   public void removeTask(String task)
   {
      List.remove(task);
      num--;
   }
   
   public void viewList()
   {
      if (num == 0)
      System.out.println("List is empty. Add a task to get started!");
      else
      {
         System.out.println("========== Viewing List ==========");
         for(int i = 0; i < num; i++)
         {
            System.out.println("- " + List.get(i));
         }
      }
   }
}