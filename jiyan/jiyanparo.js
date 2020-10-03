function S4() {
   return ((1 + Math.random()) * 65536 | 0)["toString"](16)["substring"](1);


}


function  jKCV(){
   let a = S4()+S4()+S4()+S4()
   return a
}
module.exports={
   jKCV

}


