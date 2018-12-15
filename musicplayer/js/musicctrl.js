var play = document.getElementById('play'),
	pause = document.getElementById('pause'),
	prev = document.getElementById('prev'),
	next = document.getElementById('next'),
	musicName = document.getElementById('musicName'),
	musicImg = document.getElementById('musicImg'),
	bgImage = document.getElementById('music');
	musiclist = document.getElementById('musicli');
	
	//播放滚动
var rolltimer = null; 
	currentplay=document.getElementById("currentplay"),
    scrollspace=document.getElementById("scrollspace"),
    scrollcontent=document.getElementById("scrollcontent");
    //scrollcontent1=document.getElementById("scrollcontent1");
	 
function musicrollinit(){
	 scrollspace.style.width = (scrollcontent.offsetWidth*2+20)+"px";	
	 //scrollcontent1.innerHTML = scrollcontent.innerHTML;
	 rolltimer = setInterval(mar,50) 
}
function mar(){
	//console.log(scrollcontent.offsetWidth + ' and ' +currentplay.scrollLeft);
	//console.log(scrollcontent1.innerHTML);
	if(scrollcontent.offsetWidth<=currentplay.scrollLeft*1.5){
		currentplay.scrollLeft-=scrollcontent.offsetWidth;
		clearInterval(rolltimer);
		rolltimer = setInterval(mar,3000);  
	}else{
		clearInterval(rolltimer);
		rolltimer = setInterval(mar,50);  
		currentplay.scrollLeft++;		 
	}
}
this.musicrollinit();
// 时间间隔
var INTERVAL = 100;
var angel = 0;
// 定时器
var timer = null;

var len = music.length;
var num = 0;
this.update(); //加载时自动刷新
//配置定时器，并设置回调
timer = setInterval(imgrotate, INTERVAL);


//属性设置接口
 function setCss3(obj,objAttr){
	//循环属性对象
	for(var i in objAttr){
		var newi=i;
		//判断是否存在transform-origin这样格式的属性
		if(newi.indexOf("-")>0){
			var num=newi.indexOf("-");
			newi=newi.replace(newi.substr(num,2),newi.substr(num+1,1).toUpperCase());
		}
		//考虑到css3的兼容性问题,所以这些属性都必须加前缀才行
		obj.style[newi]=objAttr[i];
		newi=newi.replace(newi.charAt(0),newi.charAt(0).toUpperCase());
		obj.style[newi]=objAttr[i];
		obj.style["webkit"+newi]=objAttr[i];
		obj.style["moz"+newi]=objAttr[i];
		obj.style["o"+newi]=objAttr[i];
		obj.style["ms"+newi]=objAttr[i];
	}
}
//旋转
function imgrotate(){
	//return;
	angel += 0.5;
	var div=document.getElementById("musicImg");//[0];
	//console.log(div+' shuang');
	setCss3(div,{transform:"rotate("+angel+"deg)"});//setCss3(div,{transform:"rotate("+angel+"deg)","transform-origin":"0 0"})
}

//selecrt show apperarence
function mouseon(obj){
	//console.log(obj);
	if(obj.tagName  == 'TR'){	
		obj.style.color = "#FFFF00";
	}
	obj.style.cursor = "pointer";
}
function mouseout(obj){
		
	obj.style.color= "#BBFFFF";
}
//update歌曲列表功能
function update(){
	for(var i = 0; i < len; i++){
		var oTr = document.createElement('tr');
		oTr.setAttribute('onmouseover','mouseon(this)');
		oTr.setAttribute('onmouseout','mouseout(this)');
		oTr.setAttribute('onclick','listplay(this)');
		
		var oTd1 = document.createElement('td');
		
		var oInput = document.createElement('input');
		oTd1.appendChild(oInput);
		oInput.setAttribute('type','checkbox');
		oInput.setAttribute('name','item');
		
		var oTd2 = document.createElement('td');
		oTd2.innerHTML = music[i][0];
		var oTd3 = document.createElement('td');
		oTd3.innerHTML = music[i][1];
		
		var oTd4 = document.createElement('td');
		var obutton = document.createElement('button');	
		obutton.setAttribute('id','playthis');
		obutton.setAttribute('onclick','listplay(this)');
		obutton.setAttribute('onmouseover','mouseon(this)');
		obutton.setAttribute('style',' position: absolute; right: 10px;background: #33A0E8;');
		obutton.innerHTML = 'play';
		oTd4.appendChild(obutton);
		
		oTr.appendChild(oTd1);
		oTr.appendChild(oTd2);
		oTr.appendChild(oTd3);
		oTr.appendChild(oTd4);
		
		var olistTable = document.getElementById('listTable');
		olistTable.appendChild(oTr);
	}
}
	
//列表播放			
function listplay(obj){
	if(obj.tagName  == 'TR'){		
		playreq(obj.rowIndex-1);
		audio.play();
		return;
	}else if(obj.tagName  == 'TD'){ 		
		playreq(obj.parentNode.parentNode.rowIndex-1);
		audio.play();
		return;
	}
	console.log('click this but unkwon object'+obj);
}	

//资源请求
function playreq(index){
	audio.src = './music/' + 'music_' + index + '.mp3';
	musicName.innerHTML = music[index][1];
	bgImage.style.backgroundImage = 'url(./image/' + 'music_' + index + '.jpg)';
	musicImg.src = './image/' + 'music_' + index + '.jpg';
	var listr = '&nbsp&nbspWelcom to listen your heart  music player *^_^* &nbsp&nbsp&nbsp&nbsp'+'当前播放:&nbsp'+music[index][1]+'&nbsp&nbsp&nbsp&nbsp下一曲:&nbsp'+music[index+1][1]+'&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp';
	musiclist.innerHTML = listr;
}
// 播放
play.onclick = function(){
	if(audio.paused){		
		audio.play();
		musiclist.innerHTML = '&nbsp&nbspWelcom to listen your heart  music player *^_^*';
	}
	
}

// 暂停
pause.onclick = function(){
	if(audio.played){
		audio.pause();
	}
}

// 上一首
prev.onclick = function(){
	num = (num + len - 1) % len;			
	playreq(num);
	audio.play();
}

// 下一首
next.onclick = function(){
	num = (num + 1) % len;
	playreq(num);
	audio.play();
}

// 自动切换下一首
audio.addEventListener('ended',function(){
	next.onclick();
},false);
