(function(){
  var im=document.querySelector('.hero-bg');if(!im)return;function go(){requestAnimationFrame(function(){im.classList.add('in');});}
  if(im.complete&&im.naturalWidth>0)go();else im.addEventListener('load',go);
})();
(function(){
  var t=document.getElementById('logoTrack');if(!t)return;var base=[].slice.call(t.children),timer;
  function build(){
    t.classList.remove('ready');
    while(t.children.length>base.length)t.removeChild(t.lastChild);
    var gap=parseFloat(getComputedStyle(t).gap)||64,w=base.reduce(function(a,i){return a+i.getBoundingClientRect().width;},0)+gap*base.length;
    var copies=Math.max(2,Math.ceil((innerWidth*2)/w)+1);
    for(var c=1;c<copies;c++)base.forEach(function(i){var k=i.cloneNode(true);k.setAttribute('alt','');k.setAttribute('aria-hidden','true');t.appendChild(k);});
    t.style.setProperty('--shift',w+'px');t.style.setProperty('--dur',Math.round(w/38)+'s');
    void t.offsetWidth;t.classList.add('ready');
  }
  if(document.readyState==='complete')build();else addEventListener('load',build);
  addEventListener('resize',function(){clearTimeout(timer);timer=setTimeout(build,200);});
})();
(function(){
  var h=document.querySelector('header');if(!h)return;if(!document.querySelector('.hero,.art-hero')){h.classList.add('scrolled');return;}function onS(){h.classList.toggle('scrolled',scrollY>40);}addEventListener('scroll',onS,{passive:true});onS();
})();
