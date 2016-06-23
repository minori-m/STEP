public class Number {
    //token & index
    String key;
    double value ;
    int index = 0;
    
    @Override
    
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        else
            return false;
        //Number otherNumber = (Number) obj;
        // nameの値として nullを許容しています。
        //return code == null ? otherNumber.getName() == null : code.equals(otherPerson.getName());
    }
    
}