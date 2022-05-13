public class Stud {
    public static Integer cnt = 0;
    public static List<Stud> students = new List<Stud>{};
    public String name = '';
    
    public Stud(String name1){
        this.name = name1;
        cnt++;
		students.add(this);        
    }
    
    static public void display(){
        for(Stud i:students){
            System.debug(i.name);
        }
    }
    
    static public void upd(String n1, String n2){
        for(Integer i = 0; i < cnt; i++){
            if(students[i].name == n1){
                students[i].name = n2;
            }
        }
    }
    
    static public void del(String name){
        for(Integer i = 0; i < cnt; i++){
            if(students[i].name == name){
                students.remove(i);
                cnt--;
            }
        }
        
    }
}
