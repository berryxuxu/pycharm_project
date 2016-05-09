/**
 * Created by berry on 2016/5/9.
 */
function Aha(name, id, money){
    this.name = name;
    this.id = id;
    this.money = money;
}

var ab = new Aha('name',2,3);
document.getElementById("ab").innerHTML= ab.name;