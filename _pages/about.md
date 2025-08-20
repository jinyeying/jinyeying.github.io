---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}
<span class='anchor' id='about-me'></span>

I am a Staff Researcher at [Tencent](https://www.tencent.com/en-us/about.html). I earned my PhD degree from <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> [National University of Singapore (NUS), Department of Electrical and Computer Engineering (ECE)](https://cde.nus.edu.sg/ece/), supervised by [Prof. Robby T. Tan](http://tanrobby.github.io/). 
I had my research internship in <img src="/files/adobe.png" alt="Adobe" width="20" height="20"> [Adobe](https://research.adobe.com/), mentored by [Prof. Connelly Barnes](http://www.connellybarnes.com/work/) and [Prof. Eli Shechtman](https://scholar.google.com/citations?user=B_FTboQAAAAJ).
Previously, I completed my M.Sc. degree at the <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> [National University of Singapore (NUS)](https://cde.nus.edu.sg/ece/); received my B.Eng. degree from the <img src="/files/UESTC.png" alt="UESTC" width="20.842" height="20"> [University of Electronic Science and Technology of China (UESTC)](https://en.uestc.edu.cn/). 

My primary research interests include Artificial Intelligence, mainly focusing on AIGC, multimodal learning, and vision-language models (VLMs). <span style="color:red"> I'm looking for self-motivated interns and full-time researchers.</span>

# 📜 Research Area
1. AIGC, Image and Video Generation, Talking Face Generation
2. Multimodal, Direct Preference Optimization (DPO), VQA
3. Image/Video Enhancement, Restoration and Decomposition 
4. Deep Learning and its Applications (e.g., Medical Images) 

# 🔬 Project
<style>
  .project-table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;          /* 固定列宽 */
  }
  .project-row td { vertical-align: top; }
  .project-row .thumb {
    width: 280px;                 /* 固定第一列宽度 */
    overflow: hidden;             /* 防止溢出 */
  }
  .project-row .info  { padding-left: 12px; }

  /* side by side 图片容器 */
  .side-by-side {
    display: flex;
    gap: 6px;                     /* 图片间距 */
    width: 100%;
  }
  .side-by-side img {
    flex: 1;
    display: block;
    object-fit: cover;
    aspect-ratio: 1/1;            /* 保持方形缩略图 */
    min-width: 0;                 /* 防止撑破 */
  }

  /* 标题 & KPI & 链接间距 */
  .papertitle_just { font-weight: 700; font-size: 1.05em; }
  .kpis { margin: 4px 0; line-height: 1.4; }
  .info a { margin-right: 8px; }

  /* 移动端：上下排且宽度自适应 */
  @media (max-width: 600px) {
    .project-row td { display:block; width:100% !important; }
    .project-row .thumb { width:100% !important; margin-bottom:12px; }
    .side-by-side { flex-direction: column; }
    .side-by-side img { width:100%; }
  }
</style>

<table class="project-table" cellspacing="0" cellpadding="10">
  <colgroup>
    <col style="width:280px">
    <col>
  </colgroup>
  <tbody>
    <!-- 1 HOK Creator -->
    <tr class="project-row">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/HOK_Creator_before.png" alt="HOK Creator before">
          <img src="./files/HOK_Creator_after.png"  alt="HOK Creator after">
        </div>
      </td>
      <td class="info">
        <a href="https://camp.honorofkings.com/studio?creator-tools=%2Fout%2Fhok-tools#/create-tools">
          <span class="papertitle_just">Honor of Kings (HOK) AIUGC Online Hero Generation</span>
        </a><br>
        <em>HOK Creator Studio</em>, 2024.12 – Present <br>
        <p class="kpis">
          <strong>44,300+</strong> Generated AI Images ·
          <strong>22%</strong> Save Rate ·
          <strong>11,400+</strong> Active Users<br>
          <strong>98</strong> Heroes ·
          <strong>12</strong> Styles ·
          <strong>13s</strong> Generation Time
        </p>
        <a href="https://camp.honorofkings.com/studio?creator-tools=%2Fout%2Fhok-tools#/create-tools">Online Generation</a> |
        <a href="https://www.bilibili.com/video/BV1vDXhY9EDG/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video(CN)</a> |
        <a href="https://youtu.be/yEi3F9aZaaU?si=2nJls3ACbN7gsabV">Video(EN)</a>
      </td>
    </tr>

    <!-- 2 HOK Poster -->
    <tr class="project-row">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/HOK_Poster_before.png" alt="HOK Poster before">
          <img src="./files/HOK_Poster_after.png"  alt="HOK Poster after">
        </div>
      </td>
      <td class="info">
        <a href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">
          <span class="papertitle_just">Honor of Kings (HOK) AIUGC DIY Poster</span>
        </a><br>
        <em>HOK Flowborn Dimensional Editor</em>, 2025.06 – Present <br>
        <p class="kpis">
          <strong>1,890,000+</strong> Posters ·
          <strong>1,020,000+</strong> Generated AI Posters (54%)<br>
          <strong>4,500+</strong> Overseas Buzz ·
          <strong>3,000+</strong> Domestic Buzz<br>
          <strong>80%</strong> In-Game Display ·
          <strong>99%</strong> Positive/Neutral Sentiment<br>
        </p>
        <a href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">Online Generation</a> |
        <a href="https://www.bilibili.com/video/BV1rS36zhEqD/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video(CN)</a> |
        <a href="https://youtu.be/BKT8AuaVNB8?si=GqO5OWlHhu5jNIL5">Video(EN)</a>
      </td>
    </tr>

    <!-- 3 HOK Conan -->
    <tr class="project-row">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/HOK_Conan_before.png" alt="HOK Conan before">
          <img src="./files/HOK_Conan_after.png"  alt="HOK Conan after">
        </div>
      </td>
      <td class="info">
        <a href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">
          <span class="papertitle_just">Honor of Kings (HOK) AIUGC Deduction Poster</span>
        </a><br>
        <em>HOK Flowborn Dimensional Editor</em>, 2025.08 – Present <br>
        <p class="kpis"></p>
        <a href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">Online Generation</a> |
        <a href="https://www.bilibili.com/video/BV1CpuPzxEGf/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video(CN)</a> |
        <a href="https://youtube.com/shorts/AUhqPP_0NIU?si=jNKspwxoQAlRcjA-">Video(EN)</a>
      </td>
    </tr>

    <!-- 4 HOK PGC -->
    <tr class="project-row">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/HOK_PGC_before.png" alt="HOK PGC before">
          <img src="./files/HOK_PGC_after.png"  alt="HOK PGC after">
        </div>
      </td>
      <td class="info">
        <a href="https://camp.honorofkings.com/studio?creator-tools=%2Fout%2Fhok-tools#/library?oneLevelTabs=51">
          <span class="papertitle_just">Honor of Kings (HOK) AIPGC Avatar/Sticker</span>
        </a><br>
        <em>HOK </em>, 2024.07 – Present <br>
        <p class="kpis">
          <strong>600,000+</strong> Explosure ·
          <strong>60,000+</strong> Engagement ·
          <strong>10+</strong> Launch <br>
        </p>
        <a href="https://camp.honorofkings.com/studio?creator-tools=%2Fout%2Fhok-tools#/library?oneLevelTabs=51">Avatar Center</a> |
        <a href="https://www.bilibili.com/video/BV1uCeFzXEkX/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video(CN)</a> |
        <a href="https://youtu.be/vdVQxsIBEes">Video(EN)</a>
      </td>
    </tr>
  </tbody>
</table>



# 📝 Publications
<style type="text/css">
    /* Color scheme stolen from Sergey Karayev */
    a {
    color: #1772d0;
    text-decoration:none !important;
    }
    a:focus, a:hover {
    color: #f09228;
    text-decoration:none !important;
    }
    table,td,th,tr{
    	border:none !important;
    }
    body,td,th,tr,p,a {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px
    }
    strong {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px;
    }
    heading {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 22px;
    }
    papertitle {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px;
    font-weight: 700
    }
    papertitle_just {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px;
    font-weight: 700;
    text-align: justify
    }
    name {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 32px;
    }
    .one
    {
    width: 160px;
    height: 160px;
    position: relative;
    }
    .two
    {
    width: 160px;
    height: 160px;
    position: absolute;
    transition: opacity .2s ease-in-out;
    -moz-transition: opacity .2s ease-in-out;
    -webkit-transition: opacity .2s ease-in-out;
    }
    .fade {
     transition: opacity .2s ease-in-out;
     -moz-transition: opacity .2s ease-in-out;
     -webkit-transition: opacity .2s ease-in-out;
    }
    span.highlight {
        background-color: #ffffd0;
    }
</style>
<!-- ################################  CONTENT START  ##################################################-->
<table width="100%" align="center" border="0" cellspacing="0" cellpadding="10">
<tbody>
<!-- ############################ Put your publications below this! ####################################-->

<!-- ###################################################################################################-->
<!-- Paper 23 PosterCraft -->
<tr onmouseout="arxiv25_PosterCraft_stop()" onmouseover="arxiv25_PosterCraft_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'arxiv25_PosterCraft_image'>
<img src="./files/arxiv25_PosterCraft_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/arxiv25_PosterCraft_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function arxiv25_PosterCraft_start() {
document.getElementById('arxiv25_PosterCraft_image').style.opacity = "1";
}
function arxiv25_PosterCraft_stop() {
document.getElementById('arxiv25_PosterCraft_image').style.opacity = "0";
}
arxiv25_PosterCraft_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2506.10741">
    <papertitle_just>PosterCraft: Rethinking High-Quality Aesthetic Poster Generation in a Unified Framework</papertitle_just>     
  </a>
  <br>
  Sixiang Chen*, Jianyu Lai*, Jialin Gao*, Tian Ye, Haoyu Chen, Hengyu Shi, Shitong Shao, Yunlong Lin, Song Fei, Zhaohu Xing, <strong>Yeying Jin</strong>, Junfeng Luo, Xiaoming Wei, Lei Zhu
  <br>
<em>arxiv</em>, 2025 <br>
<a href="https://arxiv.org/abs/2506.10741">arXiv</a>
|
<a href="https://github.com/Ephemeral182/PosterCraft"><img src="https://img.shields.io/github/stars/Ephemeral182/PosterCraft?style=social&label=Stars"></a>
| 
<a href="./files/arxiv25_PosterCraft_bibtex.txt">bibtex</a>
|
<a href="https://ephemeral182.github.io/PosterCraft/">project page</a>  
|
<a href="https://huggingface.co/spaces/Ephemeral182/PosterCraft">online demo</a>    
|
<a href="https://www.youtube.com/watch?v=92wMU4D7qx0">video</a>
|
<a href="https://mp.weixin.qq.com/s/gq6DwohKP0z333OSDRe7Xw">link</a>  
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 22 DSDNet -->
<tr onmouseout="acm25_DSDNet_stop()" onmouseover="acm25_DSDNet_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'acm25_DSDNet_image'><img src='./files/acm25_DSDNet_after.png'></div>
<img src='./files/acm25_DSDNet_before.png'>
</div>
<script type="text/javascript">
function acm25_DSDNet_start() {
document.getElementById('acm25_DSDNet_image').style.opacity = "1";
}
function acm25_DSDNet_stop() {
document.getElementById('acm25_DSDNet_image').style.opacity = "0";
}
acm25_DSDNet_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2504.15756">
    <papertitle_just>DSDNet: Raw Domain Demoiréing via Dual Color-Space Synergy</papertitle_just>     
  </a>
  <br>
  Qirui Yang, Fangpu Zhang, <strong>Yeying Jin</strong>, Qihua Cheng, Pengtao Jiang, Huanjing Yue, Jingyu Yang
  <br>
<em>ACM Multimedia (ACM'MM)</em>, 2025, Dublin, Ireland <br>
<a href="https://arxiv.org/abs/2504.15756">arXiv</a>
| 
<a href="./files/acm25_DSDNet_bibtex.txt">bibtex</a> 
|
<a href="https://xxxxxxxxdsdnet.github.io/DSDNet/">demo</a>  
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 21 PR -->
<tr onmouseout="pr25_Attacks_stop()" onmouseover="pr25_Attacks_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'pr25_Attacks_image'>
<img src="./files/pr25_Attacks.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/pr25_Attacks.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<script type="text/javascript">
function pr25_Attacks_start() {
document.getElementById('pr25_Attacks_image').style.opacity = "1";
}
function pr25_Attacks_stop() {
document.getElementById('pr25_Attacks_image').style.opacity = "0";
}
pr25_Attacks_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2504.17457">
    <papertitle_just>Unveiling Hidden Vulnerabilities in Digital Human Generation via Adversarial Attacks</papertitle_just>     
  </a>
  <br>
  Zhiying Li, <strong>Yeying Jin</strong>, Fan Shen, Zhi Liu, Weibin Chen, Pengju Zhang, Xiaomei Zhang, Boyu Chen, Michael Shen, Kejian Wu, Zhaoxin Fan, Jin Dong
  <br>
<em>Pattern Recognition (PR)</em>, 2025 <br>
<a href="https://arxiv.org/abs/2504.17457">arXiv</a>
| 
<a href="./files/pr25_Attacks_bibtex.txt">bibtex</a>  
|
<a href="https://mp.weixin.qq.com/s/xviRfqXDHGhBUOHhYuiy9A">link</a> 
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 20 GenHaze -->
<tr onmouseout="iccv25_GenHaze_stop()" onmouseover="iccv25_GenHaze_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'iccv25_GenHaze_image'>
<img src="./files/iccv25_GenHaze_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/iccv25_GenHaze_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<script type="text/javascript">
function iccv25_GenHaze_start() {
document.getElementById('iccv25_GenHaze_image').style.opacity = "1";
}
function iccv25_GenHaze_stop() {
document.getElementById('iccv25_GenHaze_image').style.opacity = "0";
}
iccv25_GenHaze_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="">
    <papertitle_just>GenHaze: Pioneering Controllable One-Step Realistic Haze Generation for Real-World Dehazing</papertitle_just>     
  </a>
  <br>
 Sixiang Chen, Tian Ye, Yunlong Lin, <strong>Yeying Jin</strong>, Yijun Yang, Haoyu Chen, Jianyu Lai, Song Fei, Zhaohu Xing, Fugee Tsung, Lei Zhu
  <br>
<em>International Conference on Computer Vision (ICCV)</em>, 2025, Hawaii, USA <br>
<a href="">arXiv</a>
| 
<a href="./files/iccv25_GenHaze_bibtex.txt">bibtex</a>  
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->


<!-- ###################################################################################################-->
<!-- Paper 19 JarvisIR -->
<tr onmouseout="cvpr25_JarvisIR_stop()" onmouseover="cvpr25_JarvisIR_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'cvpr25_JarvisIR_image'><img src='./files/cvpr25_JarvisIR_after.png'></div>
<img src='./files/cvpr25_JarvisIR_before.png'>
</div>
<script type="text/javascript">
function cvpr25_JarvisIR_start() {
document.getElementById('cvpr25_JarvisIR_image').style.opacity = "1";
}
function cvpr25_JarvisIR_stop() {
document.getElementById('cvpr25_JarvisIR_image').style.opacity = "0";
}
cvpr25_JarvisIR_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2504.04158">
    <papertitle_just>JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration</papertitle_just>     
  </a>
  <br>
  Yunlong Lin*, Zixu Lin*, Haoyu Chen*, Panwang Pan*, Chenxin Li, Sixiang Chen, Kairun Wen, <strong>Yeying Jin</strong>, Wenbo Li, Xinghao Ding
  <br>
<em>Computer Vision and Pattern Recognition (CVPR)</em>, 2025, Nashville, USA <br>
<a href="https://arxiv.org/abs/2504.04158">arXiv</a>
|
<a href="https://github.com/LYL1015/JarvisIR"><img src="https://img.shields.io/github/stars/LYL1015/JarvisIR?style=social&label=Stars"></a>
| 
<a href="./files/cvpr25_JarvisIR_bibtex.txt">bibtex</a>
|
<a href="https://cvpr2025-jarvisir.github.io/">project page</a>  
|
<a href="https://huggingface.co/spaces/LYL1015/JarvisIR">online demo</a>  
|
<a href="https://mp.weixin.qq.com/s/zYhqjMfThwwTK9nhXwYu4g">link</a>    
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 18 ntire -->
<tr onmouseout="ntire25_rd_stop()" onmouseover="ntire25_rd_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'ntire25_rd_image'><img src='./files/ntire25_raindropclarify_after.png'></div>
<img src='./files/ntire25_raindropclarify_before.png'>
</div>
<script type="text/javascript">
function ntire25_rd_start() {
document.getElementById('ntire25_rd_image').style.opacity = "1";
}
function ntire25_rd_stop() {
document.getElementById('ntire25_rd_image').style.opacity = "0";
}
ntire25_rd_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2504.12711">
    <papertitle_just>NTIRE 2025 challenge on day and night raindrop removal for dual-focused images: Methods and results</papertitle_just>
  </a>
  <br>
  Xin Li*, <strong>Yeying Jin</strong>*, Xin Jin*, etc. (Corresponding authors) 
  <br>
  <em>Computer Vision and Pattern Recognition (CVPR)</em>, 2025, Nashville, USA <br>
  <a href="https://arxiv.org/abs/2504.12711">arXiv</a>
  |
  <a href="https://github.com/jinyeying/RaindropClarity"><img src="https://img.shields.io/github/stars/jinyeying/RaindropClarity?style=social&label=Stars"></a>
  |
  <a href="./files/ntire25_raindropclarify_bibtex.txt">bibtex</a>
  |
  <a href="https://github.com/jinyeying/RaindropClarity/blob/main/poster_slides/RaindropClarity_PPT.pdf">slides</a>
  |
  <a href="https://youtu.be/YaPL0dI5l0U?si=pVniAaheEXsf5CNW">video</a>
  |
  <a href="https://codalab.lisn.upsaclay.fr/competitions/21345">competition</a>
  |
  <a href="https://lixinustc.github.io/CVPR-NTIRE2025-RainDrop-Competition.github.io/">challenge</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 17 RaindropClarity -->
<tr onmouseout="eccv24_rd_stop()" onmouseover="eccv24_rd_start()" >  
<td width="20%">
<div class="one">
<div class="two" id = 'eccv24_rd_image'><img src='./files/eccv24_raindropclarify_after.png'></div>
<img src='./files/eccv24_raindropclarify_before.png'>
</div>
<script type="text/javascript">
function eccv24_rd_start() {
document.getElementById('eccv24_rd_image').style.opacity = "1";
}
function eccv24_rd_stop() {
document.getElementById('eccv24_rd_image').style.opacity = "0";
}
eccv24_rd_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2407.16957">
    <papertitle_just>Raindrop Clarity: A Dual-Focused Dataset for Day and Night Raindrop Removal</papertitle_just>
  </a>
  <br>
  <strong>Yeying Jin</strong>, Xin Li, Jiadong Wang, Yan Zhang, Malu Zhang
  <br>
  <em>European Conference on Computer Vision (ECCV)</em>, 2024, Milan, Italy <br>
  <a href="https://arxiv.org/abs/2407.16957">arXiv</a>
  |
  <a href="https://github.com/jinyeying/RaindropClarity"><img src="https://img.shields.io/github/stars/jinyeying/RaindropClarity?style=social&label=Stars"></a>
  |
  <a href="./files/eccv24_raindropclarify_bibtex.txt">bibtex</a>
  |
  <a href="https://github.com/jinyeying/RaindropClarity/blob/main/poster_slides/RaindropClarity_poster.pdf">poster</a>
  |
  <a href="https://github.com/jinyeying/RaindropClarity/blob/main/poster_slides/RaindropClarity_PPT.pdf">slides</a>
  |
  <a href="https://www.youtube.com/watch?v=LSGvCuT46XU">video</a>
  |
  <a href="https://codalab.lisn.upsaclay.fr/competitions/21345">competition</a>
  |
  <a href="https://lixinustc.github.io/CVPR-NTIRE2025-RainDrop-Competition.github.io/">challenge</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 16 HSCR -->
<tr onmouseout="acl25_hscr_stop()" onmouseover="acl25_hscr_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'acl25_hscr_image'>
<img src='./files/HSCR_after.png' style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src='./files/HSCR_before.png' style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<script type="text/javascript">
function acl25_hscr_start() {
document.getElementById('acl25_hscr_image').style.opacity = "1";
}
function acl25_hscr_stop() {
document.getElementById('acl25_hscr_image').style.opacity = "0";
}
acl25_hscr_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2506.00805">
    <papertitle_just>HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models</papertitle_just>
  </a>
  <br>
  Songtao Jiang, Yan Zhang, <strong>Yeying Jin</strong>, Zhihang Tang, Yangyang Wu, Yang Feng, Jian Wu, Zuozhu Liu
  <br>
  <em>Association for Computational Linguistics (ACL)</em>, 2025, Vienna, Austria <br>
  <a href="https://arxiv.org/abs/2506.00805">arXiv</a>
  |
  <a href="./files/HSCR25_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 15 VQA -->
<tr onmouseout="acl25_vqa_stop()" onmouseover="acl25_vqa_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'acl25_vqa_image'>
<img src="./files/VQA_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/VQA_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<script type="text/javascript">
function acl25_vqa_start() {
document.getElementById('acl25_vqa_image').style.opacity = "1";
}
function acl25_vqa_stop() {
document.getElementById('acl25_vqa_image').style.opacity = "0";
}
acl25_vqa_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2506.00806">
    <papertitle_just>Fast or Slow? Integrating Fast Intuition and Deliberate Thinking for Enhancing Visual Question Answering</papertitle_just>
  </a>
  <br>
  Songtao Jiang, Chenyi Zhou, Yan Zhang, <strong>Yeying Jin</strong>, Zuozhu Liu
  <br>
  <em>Association for Computational Linguistics (ACL)</em>, 2025, Vienna, Austria <br>
  <a href="https://arxiv.org/abs/2506.00806">arXiv</a>
  |
  <a href="./files/VQA25_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 14 MFDPO -->
<tr onmouseout="arxiv24_dpo_stop()" onmouseover="arxiv24_dpo_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'arxiv24_dpo_image'>
<img src="./files/MFDPO_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/MFDPO_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<script type="text/javascript">
function arxiv24_dpo_start() {
document.getElementById('arxiv24_dpo_image').style.opacity = "1";
}
function arxiv24_dpo_stop() {
document.getElementById('arxiv24_dpo_image').style.opacity = "0";
}
arxiv24_dpo_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2410.15334">
    <papertitle_just>Modality-Fair Preference Optimization for Trustworthy MLLM Alignment</papertitle_just>
  </a>
  <br>
  Songtao Jiang, Yan Zhang, Ruizhe Chen, <strong>Yeying Jin</strong>, Zuozhu Liu
  <br>
  <em>International Joint Conference on Artificial Intelligence (IJCAI)</em>, 2025, Montreal, Canada <br>
  <a href="https://arxiv.org/abs/2410.15334">arXiv</a>
  |
  <a href="./files/MFDPO24_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 13 CGSAM -->
<tr onmouseout="arxiv24_CGSAM_stop()" onmouseover="arxiv24_CGSAM_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'arxiv24_CGSAM_image'>
<img src="./files/CGSAM_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/CGSAM_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<script type="text/javascript">
function arxiv24_CGSAM_start() {
document.getElementById('arxiv24_CGSAM_image').style.opacity = "1";
}
function arxiv24_CGSAM_stop() {
document.getElementById('arxiv24_CGSAM_image').style.opacity = "0";
}
arxiv24_CGSAM_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2404.04514">
    <papertitle_just>Joint Visual and Text Prompting for Improved Object-Centric Perception with Multimodal Large Language Models</papertitle_just>
  </a>
  <br>
  Songtao Jiang, Yan Zhang, Chenyi Zhou, <strong>Yeying Jin</strong>, Yang Feng, Jian Wu, Zuozhu Liu
  <br>
  <em>ADHIP Best Paper Award</em>, 2024, Jiaxing, China <br>
  <a href="https://arxiv.org/abs/2404.04514">arXiv</a>
  |
  <a href="https://github.com/jiangsongtao/VTprompt"><img src="https://img.shields.io/github/stars/jiangsongtao/VTprompt?style=social&label=Stars"></a>
  |
  <a href="./files/CGSAM24_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 12 Med-MoE -->
<tr onmouseout="emnlp24_moe_stop()" onmouseover="emnlp24_moe_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'emnlp24_moe_image'>
<img src="./files/emnlp24_moe_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/emnlp24_moe_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<script type="text/javascript">
function emnlp24_moe_start() {
document.getElementById('emnlp24_moe_image').style.opacity = "1";
}
function emnlp24_moe_stop() {
document.getElementById('emnlp24_moe_image').style.opacity = "0";
}
emnlp24_moe_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2404.10237">
    <papertitle_just>Med-MoE: Mixture of Domain-Specific Experts for Lightweight Medical Vision-Language Models</papertitle_just>
  </a>
  <br>
  Songtao Jiang, Tuo Zheng, Yan Zhang, <strong>Yeying Jin</strong>, Li Yuan, Zuozhu Liu
  <br>
  <em>EMNLP finding</em>, 2024, Miami, Florida <br>
  <a href="https://arxiv.org/abs/2404.10237">arXiv</a>
  |
  <a href="https://github.com/jiangsongtao/Med-MoE"><img src="https://img.shields.io/github/stars/jiangsongtao/Med-MoE?style=social&label=Stars"></a>
  |
  <a href="./files/emnlp24_moe_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 11 Dualrain -->
<tr onmouseout="eccv24_dualrain_stop()" onmouseover="eccv24_dualrain_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'eccv24_dualrain_image'><img src='./files/eccv24_dualrain_after.png'></div>
<img src='./files/eccv24_dualrain_before.png'>
</div>
<script type="text/javascript">
function eccv24_dualrain_start() {
document.getElementById('eccv24_dualrain_image').style.opacity = "1";
}
function eccv24_dualrain_stop() {
document.getElementById('eccv24_dualrain_image').style.opacity = "0";
}
eccv24_deualrain_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08521.pdf">
    <papertitle_just>Dual-Rain: Video Rain Removal using Assertive and Gentle Teachers</papertitle_just>     
  </a>
  <br>
  Tingting Chen*, Beibei Lin*, <strong>Yeying Jin*</strong>, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan (Equal-first authors)
  <br>
<em>European Conference on Computer Vision (ECCV)</em>, 2024, Milan, Italy <br>
<a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08521.pdf">paper</a>
|
<a href="./files/eccv24_dualrain_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 10 Super-resolution -->
<tr onmouseout="eccv24_sr_stop()" onmouseover="eccv24_sr_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'eccv24_sr_image'><img src='./files/eccv24_ucip_after.png'></div>
<img src='./files/eccv24_ucip_before.png'>
</div>
<script type="text/javascript">
function eccv24_sr_start() {
document.getElementById('eccv24_sr_image').style.opacity = "1";
}
function eccv24_sr_stop() {
document.getElementById('eccv24_sr_image').style.opacity = "0";
}
eccv24_sr_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2407.13108">
    <papertitle_just>UCIP: A Universal Framework for Compressed Image Super-Resolution using Dynamic Prompt</papertitle_just>     
  </a>
  <br>
  Xin Li, Bingchen Li, <strong>Yeying Jin</strong>, Cuiling Lan, Hanxin Zhu, Yulin Ren, Zhibo Chen
  <br>
<em>European Conference on Computer Vision (ECCV)</em>, 2024, Milan, Italy <br>
<a href="https://arxiv.org/abs/2407.13108">arXiv</a>
|
<a href="https://github.com/lixinustc/UCIP"><img src="https://img.shields.io/github/stars/lixinustc/UCIP?style=social&label=Stars"></a>
|
<a href="./files/eccv24_ucip_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 9 NightHaze -->
<tr onmouseout="submit24_nighthaze_stop()" onmouseover="submit24_nighthaze_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'submit24_nighthaze_image'><img src='./files/submit24_after.png'></div>
<img src='./files/submit24_before.png'>
</div>
<script type="text/javascript">
function submit24_nighthaze_start() {
document.getElementById('submit24_nighthaze_image').style.opacity = "1";
}
function submit24_nighthaze_stop() {
document.getElementById('submit24_nighthaze_image').style.opacity = "0";
}
submit24_nighthaze_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2403.07408">
    <papertitle_just>NightHaze: Nighttime Image Dehazing via Self-Prior Learning</papertitle_just>     
  </a>
  <br>
  Beibei Lin*, <strong>Yeying Jin*</strong>, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan (Equal-first authors)
  <br>
<em>Association for the Advancement of Artificial Intelligence (AAAI)</em>, 2025, Philadelphia, USA <br>
<a href="https://arxiv.org/abs/2403.07408">arXiv</a>
|
<a href="https://github.com/bb12346/nighthaze_codes"><img src="https://img.shields.io/github/stars/bb12346/nighthaze_codes?style=social&label=Stars"></a> 
|
<a href="./files/submit24_nighthaze_bibtex.txt">bibtex</a> 
|
<a href="https://bb12346.github.io/NightHaze/">project page</a>  
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 8 Super-resolution -->
<tr onmouseout="cvpr24_sr_stop()" onmouseover="cvpr24_sr_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'cvpr24_sr_image'><img src='./files/cvpr24_after.png'></div>
<img src='./files/cvpr24_before.png'>
</div>
<script type="text/javascript">
function cvpr24_sr_start() {
document.getElementById('cvpr24_sr_image').style.opacity = "1";
}
function cvpr24_sr_stop() {
document.getElementById('cvpr24_sr_image').style.opacity = "0";
}
cvpr24_sr_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2402.19387">
    <papertitle_just>SeD: Semantic-Aware Discriminator for Image Super-Resolution</papertitle_just>     
  </a>
  <br>
  Bingchen Li, Xin Li, Hanxin Zhu, <strong>Yeying Jin</strong>, Ruoyu Feng, Zhizheng Zhang, Zhibo Chen
  <br>
<em>Conference on Computer Vision and Pattern Recognition (CVPR)</em>, 2024, Seattle, USA <br>
<a href="https://arxiv.org/abs/2402.19387">arXiv</a>
|
<a href="https://github.com/lbc12345/SeD"><img src="https://img.shields.io/github/stars/lbc12345/SeD?style=social&label=Stars"></a>
|
<a href="./files/cvpr24_sr_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 7 DeS3 -->
<tr onmouseout="aaai24_des3_stop()" onmouseover="aaai24_des3_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'submit23_shadowdiffusion_image'><img src='./files/submit23_after.png'></div>
<img src='./files/submit23_before.png'>
</div>
<script type="text/javascript">
function aaai24_des3_start() {
document.getElementById('submit23_shadowdiffusion_image').style.opacity = "1";
}
function aaai24_des3_stop() {
document.getElementById('submit23_shadowdiffusion_image').style.opacity = "0";
}
aaai24_des3_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2211.08089">
    <papertitle_just>DeS3: Adaptive Attention-driven Self and Soft Shadow Removal using ViT Similarity</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Wei Ye, Wenhan Yang, Yuan Yuan, Robby T. Tan
  <br>
<em>Association for the Advancement of Artificial Intelligence (AAAI)</em>, 2024, Vancouver, Canada <br>
<a href="https://arxiv.org/abs/2211.08089">arXiv</a>
|
<a href="https://github.com/jinyeying/DeS3_Deshadow"><img src="https://img.shields.io/github/stars/jinyeying/DeS3_Deshadow?style=social&label=Stars"></a>
|
<a href="./files/submit23_shadowdiffusion_bibtex.txt">bibtex</a>
|
<a href="https://ojs.aaai.org/index.php/AAAI/article/view/28041">paper</a>
|
<a href="https://www.dropbox.com/scl/fi/tutat8lsd2qc172tvq0ak/DeS3_poster.pdf?rlkey=71arx5ph6cnqez6yclqtmolay&dl=0">poster</a>
|  
<a href="https://www.dropbox.com/scl/fi/x0hup1n9veohk6olc8j5e/DeS3_slides.pdf?rlkey=kquyhmx67lrs2st52324283o5&dl=0">slides</a>
<p></p>
<p>First diffusion-based shadow removal performs robustly on hard, soft and self shadows.</p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 6 NightRain -->
<tr onmouseout="aaai24_nightrain_stop()" onmouseover="aaai24_nightrain_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'aaai24_nightrain_image'><img src='./files/nightrain_after.png'></div>
<img src='./files/nightrain_before.png'>
</div>
<script type="text/javascript">
function aaai24_nightrain_start() {
document.getElementById('aaai24_nightrain_image').style.opacity = "1";
}
function aaai24_nightrain_stop() {
document.getElementById('aaai24_nightrain_image').style.opacity = "0";
}
aaai24_nightrain_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2401.00729">
    <papertitle_just>NightRain: Nighttime Video Deraining via Adaptive-Rain-Removal and Adaptive-Correction</papertitle_just>     
  </a>
  <br>
  Beibei Lin*, <strong>Yeying Jin*</strong>, Wending Yan, Wei Ye, Yuan Yuan, Sunli Zhang, Robby T. Tan (Equal-first authors)
  <br>
<em>Association for the Advancement of Artificial Intelligence (AAAI)</em>, 2024, Vancouver, Canada <br>
<a href="https://arxiv.org/abs/2401.00729">arXiv</a>
|
<a href="./files/aaai24_nightrain_bibtex.txt">bibtex</a>
|
<a href="https://www.dropbox.com/scl/fi/pe8qn2cw9lb90shfxhxp5/nightrain_poster.pdf?rlkey=dzr1wtdyxc9aq4wlc1pnucr3y&dl=0">poster</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 5 NightEnhance, ECCV'22 -->
<tr onmouseout="eccv22_nightenhance_stop()" onmouseover="eccv22_nightenhance_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'eccv22_nightenhance_image'><img src='./files/eccv22_after.jpg'></div>
<img src='./files/eccv22_before.jpg'>
</div>
<script type="text/javascript">
function eccv22_nightenhance_start() {
document.getElementById('eccv22_nightenhance_image').style.opacity = "1";
}
function eccv22_nightenhance_stop() {
document.getElementById('eccv22_nightenhance_image').style.opacity = "0";
}
eccv22_nightenhance_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2207.10564">
    <papertitle_just>Unsupervised Night Image Enhancement: When Layer Decomposition Meets Light-Effects Suppression</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Wenhan Yang, Robby T. Tan
  <br>
<em>European Conference on Computer Vision (ECCV)</em>, 2022, Tel Aviv, Israel <br>
<a href="https://arxiv.org/abs/2207.10564">arXiv</a>
|
<a href="https://github.com/jinyeying/night-enhancement"><img src="https://img.shields.io/github/stars/jinyeying/night-enhancement?style=social&label=Stars"></a>
|
<a href="./files/eccv22_nightenhance_bibtex.txt">bibtex</a>
|  
<a href="https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136970396.pdf">paper</a>
|
<a href="https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136970396-supp.pdf">supp</a>  
|
<a href="https://github.com/jinyeying/night-enhancement/blob/main/poster_slides/0982_poster.pdf">poster</a>
|
<a href="https://github.com/jinyeying/night-enhancement/blob/main/poster_slides/0982_slides.pdf">slides</a>
|
<a href="https://www.youtube.com/watch?v=0_3RiwQ8u20">video</a>
|
<a href="https://www.dropbox.com/sh/ro8fs629ldebzc2/AAD1BnNSR51_tCq7DVaLSC3Fa/light-effects?dl=0&subfolder_nav_tracking=1">data</a>
|
<a href="https://mp.weixin.qq.com/s/5wjV6R95SrQHXxqMnENAAw">link</a> 
|
<a href="https://replicate.com/cjwbw/night-enhancement">online demo</a> 
<p></p>
<p>Night image enhancement by enhancing low-light regions and suppressing light-effects regions.</p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 4 DC-ShadowNet, ICCV'21 -->
<tr onmouseout="iccv21_dcshadownet_stop()" onmouseover="iccv21_dcshadownet_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'iccv21_dcshadownet_image'><img src='./files/iccv21_after.png'></div>
<img src='./files/iccv21_before.png'>
</div>
<script type="text/javascript">
function iccv21_dcshadownet_start() {
document.getElementById('iccv21_dcshadownet_image').style.opacity = "1";
}
function iccv21_dcshadownet_stop() {
document.getElementById('iccv21_dcshadownet_image').style.opacity = "0";
}
iccv21_dcshadownet_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2207.10434">
    <papertitle_just>DC-ShadowNet: Single-Image Hard and Soft Shadow Removal Using Unsupervised Domain-Classifier Guided Network</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Aashish Sharma, Robby T. Tan
  <br>
<em>International Conference on Computer Vision (ICCV)</em>, 2021, Montreal, Canada <br>
<a href="https://arxiv.org/abs/2207.10434">arXiv</a>
|  
<a href="https://github.com/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal"><img src="https://img.shields.io/github/stars/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal?style=social&label=Stars"></a>
|  
<a href="./files/iccv21_shadow_bibtex.txt">bibtex</a>
|
<a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Jin_DC-ShadowNet_Single-Image_Hard_and_Soft_Shadow_Removal_Using_Unsupervised_Domain-Classifier_ICCV_2021_paper.pdf">paper</a>
|
<a href="https://openaccess.thecvf.com/content/ICCV2021/supplemental/Jin_DC-ShadowNet_Single-Image_Hard_ICCV_2021_supplemental.pdf">supp</a>
|
<a href="https://github.com/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal/blob/main/poster_slides/DC-ShadowNet_poster.pdf">poster</a>
|
<a href="https://github.com/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal/blob/main/poster_slides/DC-ShadowNet_slides.pdf">slides</a>
|
<a href="https://www.youtube.com/watch?v=NGftPijWLGA">video</a>
<p></p>
<p>First unsupervised hard and soft shadow removal.</p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- Paper 3 NightFog-->
<tr onmouseout="acmmm23_nightdehaze_stop()" onmouseover="acmmm23_nightdehaze_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'acmmm23_nightdehaze_image'><img src='./files/acmmm23_after.png'></div>
<img src='./files/acmmm23_before.png'>
</div>
<script type="text/javascript">
function acmmm23_nightdehaze_start() {
document.getElementById('acmmm23_nightdehaze_image').style.opacity = "1";
}
function acmmm23_nightdehaze_stop() {
document.getElementById('acmmm23_nightdehaze_image').style.opacity = "0";
}
acmmm23_nightdehaze_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2308.01738">
    <papertitle_just>Enhancing Visibility in Nighttime Haze Images Using Guided APSF and Gradient Adaptive Convolution</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin*</strong>, Beibei Lin*, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan
  <br>
<em>ACM Multimedia (ACM'MM)</em>, 2023, Ottawa, Canada <br>
<a href="https://arxiv.org/abs/2308.01738">arXiv</a>
|
<a href="https://github.com/jinyeying/nighttime_dehaze"><img src="https://img.shields.io/github/stars/jinyeying/nighttime_dehaze?style=social&label=Stars"></a>
|
<a href="./files/acmmm23_nightdehaze_bibtex.txt">bibtex</a>
|
<a href="https://dl.acm.org/doi/10.1145/3581783.3611884">paper</a>
|  
<a href="https://www.dropbox.com/scl/fi/2wo8q4y2la58a3f2kvum0/0859_poster.pdf?rlkey=7x8jbdh0o550r8pvzqugt4szs&dl=0">poster</a>
|
<a href="https://www.dropbox.com/scl/fi/2wo8q4y2la58a3f2kvum0/0859_poster.pdf?rlkey=7x8jbdh0o550r8pvzqugt4szs&dl=0">slides</a>
| 
<a href="https://www.dropbox.com/sh/7qzmb3y9akejape/AABYf2ZAqn_5vmPsOPg7KqoMa?dl=0">data</a>  
<p></p>
<p>First learning-based network handling nighttime haze and glow using APSF.</p>
</td>
</tr>
<!-- ###################################################################################################-->
  
<!-- ###################################################################################################-->
<!-- Paper 2 Reflectance, AAAI'23 -->
<tr onmouseout="aaai23_reflectance_stop()" onmouseover="aaai23_reflectance_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'aaai23_reflectance_image'><img src='./files/aaai23_after.jpg'></div>
<img src='./files/aaai23_before.jpg'>
</div>
<script type="text/javascript">
function aaai23_reflectance_start() {
document.getElementById('aaai23_reflectance_image').style.opacity = "1";
}
function aaai23_reflectance_stop() {
document.getElementById('aaai23_reflectance_image').style.opacity = "0";
}
aaai23_reflectance_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2211.14751">
    <papertitle_just>Estimating Reflectance Layer from A Single Image: Integrating Reflectance Guidance and Shadow/Specular Aware Learning</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Ruoteng Li, Wenhan Yang, Robby T. Tan
  <br>
<em>Association for the Advancement of Artificial Intelligence (AAAI)</em>, 2023, Washington DC, USA <br>
<a href="https://arxiv.org/abs/2211.14751">arXiv</a>
|
<a href="https://github.com/jinyeying/S-Aware-network"><img src="https://img.shields.io/github/stars/jinyeying/S-Aware-network?style=social&label=Stars"></a>
|
<a href="./files/aaai23_reflectance_bibtex.txt">bibtex</a> 
|
<a href="https://ojs.aaai.org/index.php/AAAI/article/view/25188">paper</a> 
|  
<a href="https://www.dropbox.com/s/epc69nk2aqsdi7v/SAware_poster.pdf?dl=0">poster</a>
|
<a href="https://www.dropbox.com/s/7f3j2d5ugifpftv/SAware_ppt.pdf?dl=0">slides</a> 
<p></p>
<p>First reflectance layer estimation that performs robustly even in the presence of shadows and specularities.</p>
</td>
</tr>
<!-- ###################################################################################################-->
  
  
<!-- ###################################################################################################-->
<!-- Paper 1 defog, ACCV'22 -->
<tr onmouseout="accv22_defog_stop()" onmouseover="accv22_defog_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'accv22_defog_image'><img src='./files/accv22_after.png'></div>
<img src='./files/accv22_before.png'>
</div>
<script type="text/javascript">
function accv22_defog_start() {
document.getElementById('accv22_defog_image').style.opacity = "1";
}
function accv22_defog_stop() {
document.getElementById('accv22_defog_image').style.opacity = "0";
}
accv22_defog_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2210.03061">
    <papertitle_just>Structure Representation Network and Uncertainty Feedback Learning for Dense Non-Uniform Fog Removal</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Wending Yan, Wenhan Yang, Robby T. Tan
  <br>
<em>Asian Conference on Computer Vision (ACCV)</em>, 2022, Macau, China <br>
<a href="https://arxiv.org/abs/2210.03061">arXiv</a>
|
<a href="https://github.com/jinyeying/FogRemoval"><img src="https://img.shields.io/github/stars/jinyeying/FogRemoval?style=social&label=Stars"></a>
|
<a href="./files/accv22_defog_bibtex.txt">bibtex</a>
|  
<a href="https://openaccess.thecvf.com/content/ACCV2022/papers/Jin_Structure_Representation_Network_and_Uncertainty_Feedback_Learning_for_Dense_Non-Uniform_ACCV_2022_paper.pdf">paper</a>
|
<a href="https://openaccess.thecvf.com/content/ACCV2022/supplemental/Jin_Structure_Representation_Network_ACCV_2022_supplemental.pdf">supp</a>
|  
<a href="https://www.dropbox.com/s/f3qjxx9jf3o7b6j/0393_poster.pdf?dl=0">poster</a>
|
<a href="https://www.dropbox.com/s/fowkes8wnyr6rb1/0393_release.pdf?dl=0">slides</a>
|  
<a href="https://www.dropbox.com/home/badweather/ACCV2022_defog/Dataset_day/Smoke">data</a>
<p></p>
<p>Dense and/or non-uniform fog removal.</p>
</td>
</tr>
<!-- ###################################################################################################-->
    

<!-- ############################ Put your publications above this! ####################################-->
</tbody></table>

# 🏫 Educations
- 01.2020-01.2024: Ph.D. (AI and Deep Learning), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore (CAP: 4.75/5.00)
- 08.2017-08.2018: M.S. (Electrical and Computer Engineering), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore
- 09.2013-07.2017: B.Eng (Electrical and Computer Engineering), <img src="/files/UESTC.png" alt="UESTC" width="20.842" height="20"> UESTC, China (GPA: 3.93/4.00)

# 👔 Internship and Work Experience
- 07.2025-Present: Staff Researcher at <img src="/files/tencent.png" alt="Tencent" width="85" height="20"> Singapore, working on AIGC.
  
- 01.2024-07.2025: Senior Researcher at <img src="/files/tencent.png" alt="Tencent" width="85" height="20"> Singapore, working on AIGC.

- 06.2023-09.2023: <img src="/files/adobe.png" alt="Adobe" width="20" height="20"> [Adobe Research Intern](https://www.adobe.com/), Creative Intelligence Lab, mentored by [Connelly Barnes](http://www.connellybarnes.com/work/), worked with [Yuqian Zhou](https://yzhouas.github.io/), [Lingzhi Zhang](https://owenzlz.github.io/), [Sohrab Amirghodsi](https://www.linkedin.com/in/sohrab-amirghodsi-a89548a3/), [Eric Kee](https://www.erickee.com/).

- 01.2019-01.2020: Machine Learning Researcher at <img src="/files/biomind.png" alt="Biomind" width="80" height="20"> Singapore, advised by [Prof. Jiashi Feng](https://sites.google.com/site/jshfeng/), worked on Biomedical Image Synthesis, Super-resolution, Tumor Segmentation and Classification, expo demo for ["Deep Learning-Based End-to-end Automatic Contouring and Automated Radiation Therapy Treatment Planning System"](https://media.neurips.cc/Conferences/NeurIPS2019/NeurIPS_Expo_Book_2019.pdf).

# 🎖 Honors and Awards
-  2nd Place, [“Yayoi Kusama × Wukong”](https://modelscope.cn/brand/view/game-wan?branch=0&tree=4), ModelScope Wan 2.1 Video Generation Challenge in 2025.
-  Tencent [Knowledge Award](https://zhuanlan.zhihu.com/p/686681635) in 2024.
-  Tencent Excellent R&D Award in 2024.
-  <img src="/files/aisg.png" alt="AISG" width="20" height="20"> [AI Singapore (AISG) Ph.D. Fellowship](https://aisingapore.org/research/phd-fellowship-programme/), Theme: Continuous Learning AI, Self-supervised Learning 

# 💻 Academic Services
- Organizer: [CVPR 2025 NTIRE](https://www.cvlai.net/ntire/2025/), [the First Challenge on Day and Night Raindrop Removal for Dual-Focused Images](https://lixinustc.github.io/CVPR-NTIRE2025-RainDrop-Competition.github.io/)
- Reviewer: ACL ARR'25, ICML'25, ICLR'25, NeurIPS'23-25, CVPR'22-25, ICCV'23-25, ECCV'22-24, AAAI'23-25, ACMMM'23-25, TPAMI'23, IJCV'24, TIP'23, MICCAI'25, CVIU'23, TCSVT'23, TVCJ'23, NEUCOM'23, ACCV'22-24, IJCAI'22, IJCNN'21, etc.
- Teaching Assistant: [EE5731 Visual Computing](https://tanrobby.github.io/teaching/ece_visual/index.html), EE5904 Neural Network (NUS ECE)

# 💬 Invited Talks
<table>
  <tr>
    <th>Topic</th>
    <th>Host</th>
    <th>Date</th>
  </tr>
  
  <tr>
    <td>AI Video Gen | When Wukong meets Yayoi Kusama</td>
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"> , Singapore </td>
    <td>05.2025</td>
  </tr>
  
  <tr>
    <td><a href="https://showlab.github.io/omg/">AI × Gaming: Creative Applications of AIGC</a></td>
    <td><img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> (invited by <a href="https://qhlin.me/">Kevin QH. Lin</a>)</td>
    <td>04.2025</td>
  </tr>
  
  <tr>
    <td>AI Generation: Inspiring Game Marketing and Development</td>
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"> , Singapore </td>
    <td>02.2025</td>
  </tr>
  
  <tr>
    <td><a href="https://www.bilibili.com/video/BV1p5bFevEgP/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Raindrop Clarity: Dual-Focused, Day and Night</a></td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>09.2024</td>
  </tr>

  <tr>
    <td><a href="https://www.bilibili.com/video/BV1wc411v7zf/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Shadow Removal using Diffusion Model</a></td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>01.2024</td>
  </tr>

  <tr>
    <td>Applications of Generative AI</td>
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"> , Singapore </td>
    <td>11.2023</td>
  </tr>
  
  <tr>
    <td>Visibility Enhancement using Generative Model</td>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei Shanghai HiSilicon</td>
    <td>07.2023</td>
  </tr>
  
  <tr>
    <td>NextCam Reading Group: Light-effects Suppression</td>
    <td><img src="/files/adobe.png" alt="Adobe" width="20" height="20"> Adobe, USA (invited by <a href="https://www.erickee.com/">Eric Kee</a>)</td>
    <td>07.2023</td>
  </tr>
  
  <tr>
    <td>Image/Video Restoration and Generation</td>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei Shanghai HiSilicon</td>
    <td>03.2023</td>
  </tr>
  
  <tr>
    <td><a href="https://www.bilibili.com/video/BV1Ca4y1C7xi/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Intrinsic Image Decomposition</a></td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>02.2023</td>
  </tr>
  
  <tr>
    <td>Diffusion Model in Image Processing</td>
    <td><img src="/files/ByteDance.png" alt="ByteDance" width="100" height="20"> (invited by <a href="https://hanshuyan.github.io/">Hanshu Yan</a>)</td>
    <td>01.2023</td>
  </tr>
  
  <tr>
    <td>Visibility Enhancement in Nighttime</td>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei, Singapore</td>
    <td>12.2022</td>
  </tr>
  
  <tr>
    <td><a href="https://www.bilibili.com/video/BV1Ec411s7at/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Unsupervised Image Restoration and Generation</a></td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>11.2022</td>
  </tr>
  
  <tr>
    <th>Poster</th>
    <th>Venue</th>
    <th>Date</th>
  </tr>
  
  <tr>
    <td>Poster Present at <a href="https://valser.org/2024/#/poster">VALSE</a></td>
    <td><img src="/files/VALSE.png" alt="VALSE" width="23.2" height="20"> Chongqing, China</td>
    <td>05.2024</td>
  </tr>
  
  <tr>
    <td>Poster Present at <a href="https://www.comp.nus.edu.sg/~leegh/svd/">Singapore Vision Day</a></td>
    <td><img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore</td>
    <td>05.2023</td>
  </tr>
  
  <tr>
    <td>Poster Present at <a href="https://aisingapore.org/ai-governance/aisg-ai-governance-research-symposium-2023/">AI Research Symposium</a></td>
    <td><img src="/files/aisg.png" alt="AISG" width="20" height="20"> AISG, Singapore</td>
    <td>01.2023</td>
  </tr>
</table>






