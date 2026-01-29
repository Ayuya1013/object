let canvas = document.getElementById("gameCanvas");
let ctx = canvas.getContext("2d");


//描画のぼやぼやをなくすメソッド
ctx.mozimageSmoothingEnabled = false;
ctx.msimageSmoothingEnabled = false;
ctx.webkitimageSmoothingEnabled = false;
ctx.imageSmoothingEnabled = false;

canvas.width  = CAN_W; //ゲーム画面サイズ横
canvas.height = CAN_H; //ゲーム画面サイズ縦

window.onload = function(){    
    loop();
} 

function draw_ball() { 
  ctx.fillStyle = "wight";
  ctx.fillRect(canvas.width >> 1, canvas.height -100 , 50, 50);
}

function draw() {
  console.log("drawball is invoked\n");

  ctx.fillStyle = "black";
  ctx.fillRect(0,0,CAN_W, CAN_H)
  draw_ball();
  // console.log("ctx.width : " + ctx.width)
  // console.log("ctx.height : " + ctx.height)
}

function update() {
  console.log("update is invoked\n");
  
}

function loop() {
  //console.log("loop is invoked\n");
  draw();
  update();
  requestAnimationFrame(loop);
}