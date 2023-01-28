let btn1 = document.getElementById("menu-btn")
let btn2 = document.getElementById("menu-bar")
let tab1 = document.getElementById("songsList")
let tab2 = document.getElementById("Player")
let sItem = document.getElementById("songListItems")
let playbtn = document.getElementsByClassName("play-btn")
let mainplaybtn = document.getElementById("main-play-btn")
let songName = document.getElementById("songName")
let MainTab = document.getElementById("MainTab")
let nextbtn = document.getElementById("next-btn")
let backbtn = document.getElementById("back-btn")
var CurrentSong = 0;
let titles = Array.from(document.getElementsByClassName("title"))

let ListOfSongs = Array.from(document.getElementsByClassName("song-item"))
var flag = 1;








// code for audioelemnt
let Myprogressbar = document.getElementById("progress")

let SongList = [
    { name: "Ee Manasse song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576805/Ee_manase_se__tribute_to_SPB_3_tholi_prema__cover_song_Koteshwar_rao_128k_bi9i3j.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892748/1_ux1n4r.jpg" },
    { name: "Aasha Pasham Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576815/AASHA_PASHAM___C_O_Kancharapalem_____23trending_23careofkancharapalem__23untrainedsinger__23coversong_128k_kbdwqy.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892748/2_nzzhzl.jpg" },
    { name: "Maguva Maguva Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576813/vakeelsaab__Maguva_maguva__cover_song_pavan_kalyan_Koteshwar_rao_128k_kshhqd.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892748/3_oiblry.jpg" },
    { name: "Manasu Dhari Thappene Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576819/Manasu_Dhari_Thappene_cover_song__ft_kotesh__Shikaru_songs__Sid_Sriram__SaiDhansika__Abhinav_128k_tptmcs.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892748/4_j6kynz.jpg" },
    { name: "Materani Chinnadhani Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576823/Materani_chinna_dhani_cover_song___SPB_koteswara_rao_256k_v70g9e.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892747/6_a7ewjl.jpg" },
    { name: "Materani Chinnadhani (Tamil)Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576806/MATERANI_CHINNADHANI__TAMIL___cover_song__spb__koteswara_rao_128k_yegxgz.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892747/6_a7ewjl.jpg" },
    { name: "Oke oka Lokam Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576818/sidsriram-oke_oka_lokam_nuvve_Sashi__koteshwar_rao_cover_song_128k_dmr8im.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892749/8_n7mhyn.jpg" },
    { name: "Oke oka Lokam (Tamil) Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576825/sidsriram-_OKE_OKA_LOKAM_lyrical___TAMIL_VERSION__SASHI__COVER_SONGKOTESHWAR_RAO_128k_vmv2tz.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892749/9_lzh3mb.jpg" },
    { name: "Pavizha Mazha Song Mp3", path: "https://res.cloudinary.com/dlj5s1kn2/video/upload/v1674576815/Pavizha_mazha_cover_song__Athiran__Fahad_Faasil__KS_Harisankar__PS_Jayhari__Vinayak_Sasikumar_128k_k4tjmo.mp3", im: "https://res.cloudinary.com/dlj5s1kn2/image/upload/v1674892749/10_mam9kc.jpg" }
]

let booleanEl = true
var Name_of_song = SongList[0].name
var path_of_song = SongList[0].path
let audioEl = new Audio(Name_of_song, path_of_song);
// code for menubars

btn1.addEventListener('click', () => {
    tab1.style.width = '0%'
    MainTab.style.width = '70%'
    tab2.style.width = '100%'
    btn2.style.visibility = "visible"
    btn1.style.visibility = "hidden"


})
btn2.addEventListener('click', () => {
    tab1.style.width = '30%'
    tab2.style.width = '100%'
    MainTab.style.width = '80%'
    btn1.style.visibility = "visible"
    btn2.style.visibility = "hidden"
    sItem.style.height = "75vh"
})


function playAudio(Name_of_song, path_of_song) {
    titles[CurrentSong].style.color = "rgb(226, 69, 200)"
    audioEl = new Audio(path_of_song)
    audioEl.play()
    songName.innerHTML = "Song Name : " + Name_of_song + "<br>   " + "Artist : Koteswara Rao"
    audioEl.addEventListener('timeupdate', () => {
        progval = parseInt((audioEl.currentTime / audioEl.duration) * 100)
        Myprogressbar.value = progval
    })
    Myprogressbar.addEventListener('change', () => {
        audioEl.currentTime = (Myprogressbar.value * audioEl.duration) / 100
    })

}


ListOfSongs.forEach((element, i) => {
    console.log(element, i)
    element.addEventListener('click', () => {
        titles[CurrentSong].style.color = "white"
        CurrentSong = element.id;
        MainTab.getElementsByTagName('img')[0].src = SongList[element.id].im
        console.log("pic updated")
        Name_of_song = SongList[element.id].name;
        path_of_song = SongList[element.id].path;
        if (audioEl.paused || audioEl.currentTime <= 0) {
            playAudio(Name_of_song, path_of_song)
            mainplaybtn.classList.remove("fa-circle-play")
            mainplaybtn.classList.add("fa-circle-pause")
        }
        else {

            audioEl.pause()
            playAudio(Name_of_song, path_of_song)
        }
    })
})
mainplaybtn.addEventListener('click', () => {
    if (audioEl.paused || audioEl.currentTime <= 0) {
        mainplaybtn.classList.remove("fa-circle-play")
        mainplaybtn.classList.add("fa-circle-pause")
        audioEl.play()
    }
    else {
        mainplaybtn.classList.remove("fa-circle-pause")
        mainplaybtn.classList.add("fa-circle-play")
        audioEl.pause()
    }
})

// code for forward and backward buttons

backbtn.addEventListener('click', () => {
    if (CurrentSong > 0) {
        titles[CurrentSong].style.color = "white"

        audioEl.pause()
        CurrentSong = CurrentSong - 1;
        Name_of_song = SongList[CurrentSong].name;
        path_of_song = SongList[CurrentSong].path;
        MainTab.getElementsByTagName('img')[0].src = SongList[CurrentSong].im
        mainplaybtn.classList.remove("fa-circle-play")
        mainplaybtn.classList.add("fa-circle-pause")

        playAudio(Name_of_song, path_of_song)
    }
    else {
        audioEl.pause()
        Name_of_song = SongList[CurrentSong].name;
        path_of_song = SongList[CurrentSong].path;
        playAudio(Name_of_song, path_of_song)
    }
})

nextbtn.addEventListener('click', () => {
    if (CurrentSong < 9) {
        titles[CurrentSong].style.color = "white"
        audioEl.pause()
        CurrentSong = (CurrentSong + 1) % 9;
        MainTab.getElementsByTagName('img')[0].src = SongList[CurrentSong].im
        Name_of_song = SongList[CurrentSong].name;
        path_of_song = SongList[CurrentSong].path;
        mainplaybtn.classList.remove("fa-circle-play")
        mainplaybtn.classList.add("fa-circle-pause")
        playAudio(Name_of_song, path_of_song)
    }
    else {
        audioEl.pause()
        Name_of_song = SongList[CurrentSong].name;
        path_of_song = SongList[CurrentSong].path;
        playAudio(Name_of_song, path_of_song)
    }
})






