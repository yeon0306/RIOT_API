window.onload = ()=>{
    const title = document.getElementById("title");

    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/');
    xhr.addEventListener("load", function() {

        let result = JSON.parse(this.responseText).r
        console.log(result)
        title.innerText = result.name + ' 레벨 : ' + result.summonerLevel;
    });
    xhr.send();
}




async function moveSearchPage(params) {
    let xhr = new XMLHttpRequest();
    const title = document.getElementById("summonerName");
    let id, puuid, name, profileiconId;

    //프로필 정보 가져오는 api call
    let getprofile = await getApi("/getSummonerInfo/"+ title.value)
    id = getprofile.id;
    puuid = getprofile.puuid;
    name = getprofile.name;
    profileiconId = getprofile.profileIconId;

    const prifileIcon = document.getElementById("profileIcon");
    prifileIcon.src = `https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/profile-icons/${profileiconId}.jpg`

    const level = document.getElementById("summonerLevel");
    level.innerText = getprofile.summonerLevel;

    const profileName = document.getElementById("summonerProfileName");
    profileName.innerText = name;

    //리그 정보 가져오는 api call
    let getleagueInfo = await getApi("/getSummonerLeagueById/"+ id);
    const summonerTier = document.getElementById("summonerTier");
    if(getleagueInfo){
        summonerTier.innerText = getleagueInfo.tier + getleagueInfo.rank + ' ' + getleagueInfo.leaguePoints + 'LP'
    }
    else {
        summonerTier.innerText = "UNRANKED"
    }

    let getMatchList = await getApi("/getMatchList/"+ puuid + '/' + 5);
    const matchList = document.getElementById("matchList");
    // matchList의 모든 자식 요소를 삭제합니다.
    while (matchList.firstChild) {
        matchList.removeChild(matchList.firstChild);
    }

    getMatchList.map(async(matchId)=>{
        let getMatchList = await getApi("/getMatchInfo/"+ matchId);
        if(getMatchList){
            const match = document.createElement("div");
            let mydata = getMatchList?.info.participants?.find((p)=>p.summonerId == id)
            match.style.marginTop = '8px'
            match.style.width = '600px'
            match.style.height = '100px'
            match.style.display = "flex"
            match.style.position = "relative"
            match.style.alignItems = "center"
            if(mydata){
                if(mydata.win)
                    match.style.backgroundColor = '#D6E6FF'
                else
                    match.style.backgroundColor = '#FFD6D6'
            }

            const cImg = document.createElement("img");
            cImg.style.width = '80px'
            cImg.style.height = '80px'
            cImg.src = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/champion/" + mydata.championName + '.png'
            match.appendChild(cImg)

            const KDALabel = document.createElement("div");
            KDALabel.style.marginLeft = "8px";
            KDALabel.innerText = mydata.kills + '/' + mydata.deaths + '/' + mydata.assists;
            match.appendChild(KDALabel)

            let gpm,xpm,dpm,dpd;
            gpm = mydata.goldEarned / (getMatchList?.info.gameDuration || 1)
            xpm = mydata.champExperience / (getMatchList?.info.gameDuration || 1)
            dpm = mydata.totalDamageDealtToChampions / (getMatchList?.info.gameDuration || 1)
            dpd = mydata.totalDamageDealtToChampions / (mydata.deaths || 1)

            let getPredict = await getApi(`/matchPredict/?gpm=${xpm}&xpm=${gpm}&dpm=${dpm}&dpd=${dpd}` );
            console.log(getPredict?.win)

            const prediction = document.createElement("div");
            prediction.style.width = '80px'
            prediction.style.height = '30px'
            prediction.style.position = "absolute"
            prediction.style.right = "0px"
            prediction.style.backgroundColor = "white"
            prediction.innerText = "예측" + (getPredict?.win > 0.5 ? "승리" : "패배");
            match.appendChild(prediction)

            matchList.appendChild(match)
        }
    })
    xhr = new XMLHttpRequest();

}

async function getApi(url, params){
    let returnValue;
    await fetch('http://127.0.0.1:8000' + url)
    .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not ok');
        }
        return response.json(); // JSON 응답을 파싱하여 JavaScript 객체로 변환
    })
    .then(data => {
        // JSON 데이터를 JavaScript 객체로 처리
        returnValue = data
      })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });

    return returnValue;
}
