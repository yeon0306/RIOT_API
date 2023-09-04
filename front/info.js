const title = document.getElementById("title"); 

const xhr = new XMLHttpRequest();
xhr.open('GET', 'http://127.0.0.1:8000/');
xhr.addEventListener("load", function() {
    let result = JSON.parse(this.responseText).r
    title.innerText = result.name + ' 레벨 : ' + result.summonerLevel;
});
xhr.send();

function search(){
    let id, name, iconId, puuid, level;
    const summonerName = document.getElementById("summonerName");

    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/getSummonerInfo/${summonerName.value}', false);
    xhr.addEventListener("load", function() {
    let result = JSON.parse(this.responseText)
    id = result.id;
    name = result.name;
    iconId = result.profileIconId;
    puuid = result.puuid;
    level = result.summonerLevel;

    const xhr2 = new XMLHttpRequest();
    xhr2.open('GET', 'http://127.0.0.1:8000/getMatchList/${puuid}/${5}');
    xhr2.addEventListener("load", function() {
        let result = JSON.parse(this.responseText)
        console.log(result)
      });
      xhr2.send();
    });
   xhr.send();
}