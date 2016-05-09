/**
 * Created by berry on 2016/4/9.
 */

function time(){
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    h = check_time(h);
    m = check_time(m);
    s = check_time(s);
    document.getElementById('time_now').innerHTML = h + ':' + m + ':' + s;
    t = setTimeout('time()',1000);
}
function check_time(i) {
    if (i < 10){
        i = '0' + i;
    }
        return i;

}

