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

I have published papers with <a href='https://scholar.google.com/citations?user=Z8PYhA4AAAAJ' target="_blank"><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> at top international venues.
📢 I'm hiring self-motivated interns and full-time researchers.

# 📜 Research {#research}
1. Video World Model
2. Agentic VLM, Agentic Video Generation
3. AIGC: Generation & Vision
4. Multimodal Learning & VLMs

# 🔬 Projects {#projects}
<div class="pub-filters" id="proj-topic-filters">
  <button class="pub-filter-btn proj-filter-btn active" data-cat="all" onclick="filterProjects('all')">All</button>
  <button class="pub-filter-btn proj-filter-btn" data-cat="world-model" onclick="filterProjects('world-model')">World Model</button>
  <button class="pub-filter-btn proj-filter-btn" data-cat="gen-vision" onclick="filterProjects('gen-vision')">Generation & Vision</button>
</div>
<div class="pub-filters" style="margin-top:4px;">
  <button class="role-filter-btn proj-role-btn active" data-role="all" onclick="filterProjRole('all')">All Roles</button>
  <button class="role-filter-btn proj-role-btn" data-role="first-author" onclick="filterProjRole('first-author')">First Author</button>
  <button class="role-filter-btn proj-role-btn" data-role="corr-author" onclick="filterProjRole('corr-author')"><sup class="corr-lead">†</sup> Corresponding Author</button>
  <button class="role-filter-btn proj-role-btn" data-role="proj-lead" onclick="filterProjRole('proj-lead')"><sup class="corr-lead">‡</sup> Project Lead</button>
</div>
<script>
var _projTopic = 'all', _projRole = 'all';
function filterProjects(cat) {
  _projTopic = cat;
  _applyProjFilter();
  document.querySelectorAll('.proj-filter-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.cat === cat);
  });
}
function filterProjRole(role) {
  _projRole = (_projRole === role) ? 'all' : role;
  _applyProjFilter();
  document.querySelectorAll('.proj-role-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.role === _projRole);
  });
}
function _applyProjFilter() {
  document.querySelectorAll('tr.project-row[data-proj-cat]').forEach(function(tr) {
    var topicOk = _projTopic === 'all' || tr.getAttribute('data-proj-cat') === _projTopic;
    var roleOk  = _projRole  === 'all' || (tr.getAttribute('data-proj-role') || '').split(' ').indexOf(_projRole) !== -1;
    tr.style.display = (topicOk && roleOk) ? '' : 'none';
  });
}
</script>
<style>
  .project-table { width: 100%; border-collapse: collapse; table-layout: fixed; }
  .project-row td { vertical-align: top; }
  .project-row .thumb { width: 280px; overflow: hidden; }
  .project-row .info  { padding-left: 12px; }

  /* side by side 图片容器 */
  .side-by-side { display: flex; gap: 6px; width: 100%; }
  .side-by-side img {
    flex: 1; display: block; object-fit: cover; aspect-ratio: 1/1; min-width: 0;
    border-radius: 12px;
  }

  /* 标题 / 副标题 / KPI：让 Demo 更贴近、更紧凑 */
  .papertitle_just {
    font-weight: 700;
    font-size: 1.05em;
    display: inline-block;
    margin-bottom: 2px;
    line-height: 1.25;
  }
  .sub {
    color:#667085;
    margin: 0 0 4px;      /* 原来 8px -> 更紧凑 */
    display: block;       /* 比 inline-block 更稳定 */
    line-height: 1.3;
  }
  .kpis {
    margin: 2px 0 4px;    /* 原来 6px 0 -> 压缩 KPI 与 Demo 的距离 */
    line-height: 1.35;    /* 原来 1.5 -> 更紧凑 */
  }
  /* 去掉 <p> 默认 margin，避免把 Demo 顶下去（关键） */
  .project-row .info p { margin-block-start: 0; margin-block-end: 0; }

  /* 链接 pill */
  .links { display:flex; align-items:center; gap:8px; margin-top: 4px; flex-wrap: wrap; }
  .links .label { color:#667085; }
  .pill {
    display:inline-block; padding:4px 10px; border-radius:999px;
    background:#f2f4f7; text-decoration:none; font-size:14px;
  }
  .pill:hover { background:#e6e9ef; }

  /* 移动端 */
  @media (max-width: 600px) {
    .project-table { display:block; width:100% !important; overflow-x:hidden; }
    .project-table colgroup { display:none; }
    .project-table tbody { display:block; width:100%; }
    .project-row { display:block; width:100%; margin-bottom:16px; }
    .project-row td { display:block; width:100% !important; box-sizing:border-box; }
    .project-row .thumb { width:100% !important; margin-bottom:8px; padding:0; }
    .side-by-side { flex-direction: row; width:100%; }
    .side-by-side img { height: 140px; width: 50%; flex: none; object-fit: cover; }
    .project-row .info { padding-left: 0; padding-top:0; font-size: 0.9em; }
  }
</style>

<table class="project-table" cellspacing="0" cellpadding="10">
  <colgroup>
    <col style="width:280px"><col>
  </colgroup>
  <tbody>


    <!-- ReactiveGWM -->
    <tr class="project-row" data-proj-cat="world-model" data-proj-role="corr-author proj-lead">
      <td class="thumb">
        <video autoplay loop muted playsinline
          style="width:100%; aspect-ratio:1/1; object-fit:cover;">
          <source src="./files/reactivegwm_demo.mp4" type="video/mp4" />
        </video>
      </td>
      <td class="info">
        <a href="https://inv-wzq.github.io/ReactiveGWM/">
          <span class="papertitle_just">ReactiveGWM: Steering NPC in Reactive Game World Models</span>
        </a><br>
        Zeqing Wang, Danze Chen, Zhaohu Xing, Zizhao Tong, Yinhan Zhang, Xingyi Yang<sup class="corr-lead">†</sup>, <strong>Yeying Jin</strong><sup class="corr-lead">†‡</sup><br>
        <div class="links">
          <a class="pill" href="https://inv-wzq.github.io/ReactiveGWM/">Project Page</a>
          <a class="pill" href="https://arxiv.org/abs/2605.15256">arXiv</a>
          <a href="https://github.com/INV-WZQ/ReactiveGWM"><img src="https://img.shields.io/github/stars/INV-WZQ/ReactiveGWM?style=social&cacheSeconds=86400" alt="GitHub stars"></a>
          <a class="pill" href="https://huggingface.co/INV-WZQ/ReactiveGWM-Models">Model</a>
          <a class="pill" href="https://huggingface.co/datasets/INV-WZQ/ReactiveGWM-Datasets">Dataset</a>
        </div>
        <span class="sub" style="display:block; margin-top:8px; line-height:1.5;">A game world model where NPCs follow high-level strategies (Offense / Defense / Control) via cross-attention — not just background pixels.<br>The strategy module transfers zero-shot to a new game without retraining.</span>
      </td>
    </tr>

    <!-- SCOPE -->
    <tr class="project-row" data-proj-cat="world-model" data-proj-role="corr-author proj-lead">
      <td class="thumb">
        <video autoplay loop muted playsinline
          style="width:100%; aspect-ratio:1/1; object-fit:cover;">
          <source src="./files/scope_demo.mp4" type="video/mp4" />
        </video>
      </td>
      <td class="info">
        <a href="https://z2tong.github.io/SCOPE/">
          <span class="papertitle_just">SCOPE: Scalable World Model via Consistent Prediction</span>
        </a><br>
        Zizhao Tong, <strong>Yeying Jin</strong><sup class="corr-lead">†‡</sup>, Hongfeng Lai, Zeqing Wang, Zhaohu Xing, Kexu Cheng, Haoran Xu, Zhao Pu, Shangwen Zhu, Ruili Feng, Jian Zhao, Yan Zhang, Hao Tang, Ling Shao<sup class="corr-lead">†</sup><br>
        <div class="links">
          <a class="pill" href="https://z2tong.github.io/SCOPE/">Project Page</a>
          <a class="pill" href="https://arxiv.org/abs/2605.23345">arXiv</a>
          <a href="https://github.com/z2tong/SCOPE"><img src="https://img.shields.io/github/stars/z2tong/SCOPE?style=social&cacheSeconds=86400" alt="GitHub stars"></a>
          <a class="pill" href="https://huggingface.co/zizhaotong/SCOPE">Model</a>
          <a class="pill" href="https://huggingface.co/collections/zizhaotong/crossfps">Dataset</a>
          <a class="pill" href="https://mp.weixin.qq.com/s/G-MkB84-rH8rEVT3m4UPTw">Link</a>
        </div>
        <span class="sub" style="display:block; margin-top:8px; line-height:1.5;">An interactive world model for FPS games.<br>Handles dense controls by learning per-pixel temporal action responses.<br>Includes CrossFPS: the first multi-game FPS dataset (69K clips, 7 titles, 10-DoF).</span>
      </td>
    </tr>

    <!-- Incantation -->
    <tr class="project-row" data-proj-cat="world-model" data-proj-role="corr-author proj-lead">
      <td class="thumb">
        <video autoplay loop muted playsinline
          style="width:100%; aspect-ratio:1/1; object-fit:cover;">
          <source src="./files/incantation_demo.mp4" type="video/mp4" />
        </video>
      </td>
      <td class="info">
        <a href="https://matrixteam-ai.github.io/pages/Incanation">
          <span class="papertitle_just">Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models</span>
        </a><br>
        Shangwen Zhu, Qianyu Peng, Zhao Pu, Zhilei Shu, Xiangrui Ke, Zhaohu Xing, Zizhao Tong, Zeqing Wang, Xinyu Cui, Huangji Wang, Jian Zhao, <strong>Yeying Jin</strong><sup class="corr-lead">‡</sup>, Fan Cheng<sup class="corr-lead">†</sup>, Ruili Feng<sup class="corr-lead">†</sup><br>
        <div class="links">
          <a class="pill" href="https://matrixteam-ai.github.io/pages/Incanation">Project Page</a>
          <a class="pill" href="https://arxiv.org/abs/2605.18601">arXiv</a>
          <a href="https://github.com/zhushangwen/Incantation"><img src="https://img.shields.io/github/stars/zhushangwen/Incantation?style=social&cacheSeconds=86400" alt="GitHub stars"></a>
          <a class="pill" href="https://huggingface.co/datasets/zhush/incantation-elden-ring-scenes">Dataset</a>
        </div>
        <span class="sub" style="display:block; margin-top:8px; line-height:1.5;">Natural language as the action interface for multi-entity control.<br>Enables cross-entity transfer (89% vs 43% for action IDs) and out-of-vocabulary control.</span>
      </td>
    </tr>

    <!--  Hero 1 -->
    <tr class="project-row" data-proj-cat="gen-vision" data-proj-role="first-author">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/Hero_before.png" alt="Hero before">
          <img src="./files/Hero_after.png"  alt="Hero after">
        </div>
      </td>
      <td class="info">
        <a href="http://16.78.125.86:7890/">
          <span class="papertitle_just">AI Photobooth</span>
        </a><br>
        <span class="sub"><em>AI Photobooth</em> • 2025.12 </span>
        <p class="kpis">
          <strong>370+</strong> Generated AI Images in 1 hour · <strong>Top 3</strong> Popular<br>
          <strong>6</strong> Heroes · <strong>2</strong> Styles · <strong>3</strong> Games
        </p>
        <div class="links">
          <span class="label">Demo:</span>
          <a class="pill" href="http://16.78.125.86:7890">Online Generation</a>
          <a class="pill" href="https://www.bilibili.com/video/BV114B5ByEbg/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video (CN)</a>
          <a class="pill" href="https://youtu.be/barpL674x7Q?si=mZQf9cKKFnzQcefj">Video (EN)</a>
        </div>
      </td>
    </tr>
  
    <!--  HOK Poster 2, 3 -->
    <tr class="project-row" data-proj-cat="gen-vision" data-proj-role="first-author">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/HOK_AI_before.png" alt="HOK Conan before">
          <img src="./files/HOK_Conan_after.png"  alt="HOK Conan after">
        </div>
      </td>
      <td class="info">
        <a href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">
          <span class="papertitle_just">Honor of Kings (HOK) AIUGC Detective & Esports Poster</span>
        </a><br>
        <span class="sub"><em>HOK Flowborn Dimensional Editor</em> • 2025.08–Present</span>
        <p class="kpis">
          <strong>Millions+</strong> Generated AI Posters, Camp First Page<br>
          <strong>Battle Loading, In-Game Hero,</strong> In-Game Popup<br>
          <strong>One-Click</strong> Sharing on HOK Camp, X, Instagram, Facebook<br>
        </p>
        <div class="links">
          <span class="label">Demo:</span>
          <a class="pill" href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">Online Generation</a>
          <a class="pill" href="https://www.bilibili.com/video/BV1CpuPzxEGf/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video (CN)</a>
          <a class="pill" href="https://youtube.com/shorts/AUhqPP_0NIU?si=jNKspwxoQAlRcjA-">Video (EN)</a>
        </div>
      </td>
    </tr>
    
    <!--  HOK Poster 1 -->
    <tr class="project-row" data-proj-cat="gen-vision" data-proj-role="first-author">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/HOK_Poster_before.png" alt="HOK Poster before">
          <img src="./files/HOK_Poster_after.png"  alt="HOK Poster after">
        </div>
      </td>
      <td class="info">
        <a href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">
          <span class="papertitle_just">Honor of Kings (HOK) AIUGC Portrait Poster</span>
        </a><br>
        <span class="sub"><em>HOK Flowborn Dimensional Editor</em> • 2025.06–Present</span>
        <p class="kpis">
          <strong>Millions+</strong> Generated AI Posters <br>
          <strong>Thousands+</strong> Overseas & Domestic Mentions<br>
          <strong>80%</strong> In-Game Display · <strong>99%</strong> Positive/Neutral Sentiment
        </p>
        <div class="links">
          <span class="label">Demo:</span>
          <a class="pill" href="https://camp.honorofkings.com/h5/app/index.html#/poster-design/home">Online Generation</a>
          <a class="pill" href="https://www.douyin.com/video/7523274499287518523">Video (CN)</a>
          <a class="pill" href="https://youtu.be/BKT8AuaVNB8?si=GqO5OWlHhu5jNIL5">Video (EN)</a>
        </div>
      </td>
    </tr>

    <!-- HOK Creator -->
    <tr class="project-row" data-proj-cat="gen-vision" data-proj-role="first-author">
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
        <span class="sub"><em>HOK Creator Studio</em> • 2024.12–Present</span>
        <p class="kpis">
          <strong>Tens of Thousands+</strong> Generated AI Images · <strong>22%</strong> Save Rate<br>
          <strong>Tens of Thousands+</strong> UV · <strong>Tens of Thousands+</strong> Active Users<br>
          <strong>98</strong> Heroes · <strong>12</strong> Styles · <strong>13S</strong> Generation Time
        </p>
        <div class="links">
          <span class="label">Demo:</span>
          <a class="pill" href="https://camp.honorofkings.com/studio?creator-tools=%2Fout%2Fhok-tools#/create-tools">Online Generation</a>
          <a class="pill" href="https://www.bilibili.com/video/BV1vDXhY9EDG/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video (CN)</a>
          <a class="pill" href="https://youtu.be/yEi3F9aZaaU?si=2nJls3ACbN7gsabV">Video (EN)</a>
        </div>
      </td>
    </tr>

    <!-- HOK PGC -->
    <tr class="project-row" data-proj-cat="gen-vision" data-proj-role="first-author">
      <td class="thumb">
        <div class="side-by-side">
          <img src="./files/HOK_PGC_before.png" alt="HOK PGC before">
          <img src="./files/HOK_PGC_after.png"  alt="HOK PGC after">
        </div>
      </td>
      <td class="info">
        <a href="https://camp.honorofkings.com/studio?creator-tools=%2Fout%2Fhok-tools#/library?oneLevelTabs=51">
          <span class="papertitle_just">Honor of Kings (HOK) AIPGC Avatars/Stickers</span>
        </a><br>
        <span class="sub"><em>HOK Avatar Center</em> • 2024.07–Present</span>
        <p class="kpis">
          <strong>12×</strong> Launch ·<strong>98</strong> Heroes · <strong>2</strong> Styles · <strong>2</strong> Halloween Topics <br>
          <strong>Over Half a Million+</strong> Exposure, <strong>Tens of K+</strong> Engagement <br>
          Available on HOK Camp, VK, X, Instagram, Facebook,<br>
          WhatsApp, Discord, Sticker
        </p>
        <div class="links">
          <span class="label">Demo:</span>
          <a class="pill" href="https://camp.honorofkings.com/studio?creator-tools=%2Fout%2Fhok-tools#/library?oneLevelTabs=51">Avatar Center</a>
          <a class="pill" href="https://www.bilibili.com/video/BV1eHe5zPEVk/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292">Video (CN)</a>
          <a class="pill" href="https://youtu.be/vdVQxsIBEes">Video (EN)</a>
        </div>
      </td>
    </tr>
  </tbody>
</table>



# 📝 Publications {#publications}
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
    font-size: 14px;
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
    font-weight: 700;
    }
    papertitle_just {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px;
    font-weight: 700;
    text-align: justify;
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
    table td em { color: #555; }
    .pub-filters { margin: 8px 0 12px 0; }
    .pub-filter-btn {
        display: inline-block; margin: 3px 4px 3px 0;
        padding: 4px 14px; border-radius: 20px; font-size: 13px;
        cursor: pointer; border: 1.5px solid #ccc;
        background: #f8f8f8; color: #444; font-weight: 500;
        transition: all .15s;
    }
    .pub-filter-btn:hover { border-color: #1772d0; color: #1772d0; background: #eef3fb; }
    .pub-filter-btn.active { background: #1772d0; color: #fff; border-color: #1772d0; }
    sup.eq-contrib { color: #f09228; font-weight: bold; }
    sup.corr-lead  { color: #1772d0; }
    .role-filter-btn {
        display: inline-block; margin: 2px 3px 2px 0;
        padding: 2px 10px; border-radius: 20px; font-size: 12px;
        cursor: pointer; border: 1px solid #ddd;
        background: #fafafa; color: #666; font-weight: 500;
        transition: all .15s;
    }
    .role-filter-btn:hover { border-color: #888; color: #333; }
    .role-filter-btn.active { background: #eef3fb; color: #1772d0; border-color: #1772d0; font-weight: 600; }
</style>
<!-- ################################  CONTENT START  ##################################################-->
<div class="pub-filters" id="pub-topic-filters">
  <button class="pub-filter-btn active" data-cat="all" onclick="filterPubs('all')">All</button>
  <button class="pub-filter-btn" data-cat="world-model" onclick="filterPubs('world-model')">World Model</button>
  <button class="pub-filter-btn" data-cat="agentic-vlm" onclick="filterPubs('agentic-vlm')">Agentic VLM</button>
  <button class="pub-filter-btn" data-cat="gen-vision" onclick="filterPubs('gen-vision')">Gen & Vision</button>
  <button class="pub-filter-btn" data-cat="multimodal" onclick="filterPubs('multimodal')">Multimodal</button>
  <button class="pub-filter-btn" data-cat="workshop" onclick="filterPubs('workshop')">Workshops</button>
  <button class="pub-filter-btn" data-cat="security" onclick="filterPubs('security')">Security</button>
</div>
<div class="pub-filters" style="margin-top:4px;">
  <button class="role-filter-btn pub-role-btn active" data-role="all" onclick="filterPubRole('all')">All Roles</button>
  <button class="role-filter-btn pub-role-btn" data-role="first-author" onclick="filterPubRole('first-author')">First Author</button>
  <button class="role-filter-btn pub-role-btn" data-role="eq-contrib" onclick="filterPubRole('eq-contrib')"><sup class="eq-contrib">*</sup> Equal Contribution</button>
  <button class="role-filter-btn pub-role-btn" data-role="corr-author" onclick="filterPubRole('corr-author')"><sup class="corr-lead">†</sup> Corresponding Author</button>
  <button class="role-filter-btn pub-role-btn" data-role="proj-lead" onclick="filterPubRole('proj-lead')"><sup class="corr-lead">‡</sup> Project Lead</button>
</div>
<script>
var _pubTopic = 'all', _pubRole = 'all';
function filterPubs(cat) {
  _pubTopic = cat;
  _applyPubFilter();
  document.querySelectorAll('#pub-topic-filters .pub-filter-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.cat === cat);
  });
}
function filterPubRole(role) {
  _pubRole = (_pubRole === role) ? 'all' : role;
  _applyPubFilter();
  document.querySelectorAll('.pub-role-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.role === _pubRole);
  });
}
function _applyPubFilter() {
  document.querySelectorAll('tr[data-category]').forEach(function(tr) {
    var topicOk = _pubTopic === 'all' || tr.dataset.category === _pubTopic;
    var roleOk  = _pubRole  === 'all' || (tr.dataset.role || '').split(' ').indexOf(_pubRole) !== -1;
    tr.style.display = (topicOk && roleOk) ? '' : 'none';
  });
}
</script>
<table width="100%" align="center" border="0" cellspacing="0" cellpadding="10">
<tbody>
<!-- ############################ Put your publications below this! ####################################-->

<!-- ###################################################################################################-->
<!-- Paper CVPR26 Deraining -->
<tr data-category="gen-vision" data-role="corr-author proj-lead" onmouseout="cvpr26_Deraining_stop()" onmouseover="cvpr26_Deraining_start()" >
<td width="20%">
<div class="one">
<div class="two" id='cvpr26_Deraining_image'>
<img src="./files/cvpr26_Deraining_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/cvpr26_Deraining_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function cvpr26_Deraining_start() {
document.getElementById('cvpr26_Deraining_image').style.opacity = "1";
}
function cvpr26_Deraining_stop() {
document.getElementById('cvpr26_Deraining_image').style.opacity = "0";
}
cvpr26_Deraining_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2605.00719">
    <papertitle_just>Unpaired Image Deraining Using Reward-Guided Self-Reinforcement Strategy</papertitle_just>
  </a>
  <br>
  Yinghao Chen, <strong>Yeying Jin</strong><sup class="corr-lead">†‡</sup>, Xiang Chen, Yanyan Wei<sup class="corr-lead">†</sup>, Ziyang Yan, Yaowei Fu
  <br>
  <em>IEEE Conference on Computer Vision and Pattern Recognition (CVPR)</em>, 2026, Denver, USA<br>
<a href="https://arxiv.org/abs/2605.00719">arXiv</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper Agentic World Modeling -->
<tr data-category="world-model" onmouseout="arxiv26_AgenticWM_stop()" onmouseover="arxiv26_AgenticWM_start()" >
<td width="20%">
<div class="one">
<div class="two" id='arxiv26_AgenticWM_image'>
<img src="./files/arxiv26_AgenticWM.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/arxiv26_AgenticWM.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function arxiv26_AgenticWM_start() {
document.getElementById('arxiv26_AgenticWM_image').style.opacity = "1";
}
function arxiv26_AgenticWM_stop() {
document.getElementById('arxiv26_AgenticWM_image').style.opacity = "0";
}
arxiv26_AgenticWM_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2604.22748">
    <papertitle_just>Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond</papertitle_just>
  </a>
  <br>
  Meng Chu<sup class="eq-contrib">*</sup>, Xuan Billy Zhang<sup class="eq-contrib">*</sup>, Kevin Qinghong Lin<sup class="eq-contrib">*</sup>, Lingdong Kong<sup class="eq-contrib">*</sup>, Jize Zhang<sup class="eq-contrib">*</sup>, Teng Tu<sup class="eq-contrib">*</sup>, Weijian Ma<sup class="eq-contrib">*</sup>, Ziqi Huang, Senqiao Yang, Wei Huang, <strong>Yeying Jin</strong>, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che<sup class="corr-lead">†</sup>, Long Chen<sup class="corr-lead">†</sup>, Qifeng Chen<sup class="corr-lead">†</sup>, Wenxuan Zhang<sup class="corr-lead">†</sup>, Wenya Wang<sup class="corr-lead">†</sup>, Xiaojuan Qi<sup class="corr-lead">†</sup>, Yang Deng<sup class="corr-lead">†</sup>, Yanwei Li<sup class="corr-lead">†</sup>, Mike Zheng Shou<sup class="corr-lead">†</sup>, Zhi-Qi Cheng<sup class="corr-lead">†</sup>, See-Kiong Ng<sup class="corr-lead">†</sup>, Ziwei Liu<sup class="corr-lead">†</sup>, Philip Torr<sup class="corr-lead">†</sup>, Jiaya Jia<sup class="corr-lead">†</sup>
  <br>
  <em>arXiv preprint</em>, 2026<br>
<a href="https://arxiv.org/abs/2604.22748">arXiv</a>
|
<a href="https://github.com/matrix-agent/awesome-agentic-world-modeling"><img src="https://img.shields.io/github/stars/matrix-agent/awesome-agentic-world-modeling?style=social&cacheSeconds=86400"></a>
|
<a href="https://agentic-world-modeling.xyz/">Project Page</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper CT-1 -->
<tr data-category="gen-vision" >
<td width="20%">
<video autoplay loop muted playsinline style="width:100%; aspect-ratio:1/1; object-fit:cover;">
  <source src="./files/ct1_demo.mp4" type="video/mp4">
</video>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2604.09201">
    <papertitle_just>CT-1: Vision-Language-Camera Models Transfer Spatial Reasoning Knowledge to Camera-controllable Video Generation</papertitle_just>
  </a>
  <br>
  Haoyu Zhao, Zihao Zhang, Jiaxi Gu, Haoran Chen, Qingping Zheng, Pin Tang, <strong>Yeying Jin</strong>, Yuang Zhang, Junqi Cheng, Zenghui Lu, Peng Shu, Zuxuan Wu<sup class="corr-lead">†</sup>, Yu-Gang Jiang<sup class="corr-lead">†</sup>
  <br>
  <em>arXiv preprint</em>, 2026<br>
  <a href="https://arxiv.org/abs/2604.09201">arXiv</a>
  |
  <a href="https://github.com/gulucaptain/Camera-Transformer-1"><img src="https://img.shields.io/github/stars/gulucaptain/Camera-Transformer-1?style=social&cacheSeconds=86400"></a>
  |
  <a href="https://gulucaptain.github.io/Camera-Transformer-1/">Project Page</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper InstanceAnimator -->
<tr data-category="gen-vision" data-role="proj-lead" onmouseout="arxiv25_InstanceAnimator_stop()" onmouseover="arxiv25_InstanceAnimator_start()" >
<td width="20%">
<div class="one">
<div class="two" id='arxiv25_InstanceAnimator_image'>
<img src="./files/arxiv25_InstanceAnimator_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/arxiv25_InstanceAnimator_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function arxiv25_InstanceAnimator_start() {
document.getElementById('arxiv25_InstanceAnimator_image').style.opacity = "1";
}
function arxiv25_InstanceAnimator_stop() {
document.getElementById('arxiv25_InstanceAnimator_image').style.opacity = "0";
}
arxiv25_InstanceAnimator_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2603.25357">
    <papertitle_just>InstanceAnimator: Multi-Instance Sketch Video Colorization</papertitle_just>
  </a>
  <br>
  Yinhan Zhang<sup class="eq-contrib">*</sup>, Yue Ma<sup class="eq-contrib">*</sup>, Bingyuan Wang, Kunyu Feng, <strong>Yeying Jin</strong><sup class="corr-lead">‡</sup>, Qifeng Chen, Anyi Rao, Zeyu Wang<sup class="corr-lead">†</sup>
  <br>
  <em>arXiv preprint</em>, 2026<br>
  <a href="https://arxiv.org/abs/2603.25357">arXiv</a> |
  <a href="https://github.com/YinHan-Zhang/InstanceAnimator"><img src="https://img.shields.io/github/stars/YinHan-Zhang/InstanceAnimator?style=social&cacheSeconds=86400"></a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper Z-Erase -->
<tr data-category="gen-vision" data-role="proj-lead" onmouseout="icml26_zerase_stop()" onmouseover="icml26_zerase_start()" >
<td width="20%">
<div class="one">
<div class="two" id='icml26_zerase_image'>
<img src="./files/icml26_zerase_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/icml26_zerase_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function icml26_zerase_start() {
document.getElementById('icml26_zerase_image').style.opacity = "1";
}
function icml26_zerase_stop() {
document.getElementById('icml26_zerase_image').style.opacity = "0";
}
icml26_zerase_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2603.25074">
    <papertitle_just>Z-Erase: Enabling Concept Erasure in Single-Stream Diffusion Transformers</papertitle_just>
  </a>
  <br>
  Nanxiang Jiang, Zhaoxin Fan<sup class="corr-lead">†</sup>, Baisen Wang, Daiheng Gao, Junhang Cheng, Jifeng Guo, Yalan Qin, <strong>Yeying Jin</strong><sup class="corr-lead">‡</sup>, Hongwei Zheng, Faguo Wu<sup class="corr-lead">†</sup>, Wenjun Wu
  <br>
  <em>International Conference on Machine Learning (ICML)</em>, 2026, Seoul, South Korea<br>
  <a href="https://arxiv.org/abs/2603.25074">arXiv</a> |
  <a href="https://github.com/nxjiang-jnx/Z-Erase"><img src="https://img.shields.io/github/stars/nxjiang-jnx/Z-Erase?style=social&cacheSeconds=86400"></a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper ReFlux -->
<tr data-category="gen-vision" onmouseout="cvpr26_ReFlux_stop()" onmouseover="cvpr26_ReFlux_start()" >
<td width="20%">
<div class="one">
<div class="two" id='cvpr26_ReFlux_image'>
<img src="./files/cvpr26_ReFlux_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/cvpr26_ReFlux_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function cvpr26_ReFlux_start() {
document.getElementById('cvpr26_ReFlux_image').style.opacity = "1";
}
function cvpr26_ReFlux_stop() {
document.getElementById('cvpr26_ReFlux_image').style.opacity = "0";
}
cvpr26_ReFlux_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2510.00635">
    <papertitle_just>Erased, But Not Forgotten: Erased Rectified Flow Transformers Still Remain Unsafe Under Concept Attack</papertitle_just>
  </a>
  <br>
  Nanxiang Jiang, Zhaoxin Fan<sup class="corr-lead">†</sup>, Enhan Kang, Daiheng Gao, Yun Zhou, Yanxia Chang, Zheng Zhu, <strong>Yeying Jin</strong>, Wenjun Wu
  <br>
  <em>IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Findings</em>, 2026, Denver, USA<br>
<a href="https://arxiv.org/abs/2510.00635">arXiv</a> |
<a href="https://github.com/nxjiang-jnx/ReFlux"><img src="https://img.shields.io/github/stars/nxjiang-jnx/ReFlux?style=social&cacheSeconds=86400"></a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper VLM-IMI -->
<tr data-category="gen-vision" data-role="proj-lead" onmouseout="cvpr26_VLM_stop()" onmouseover="cvpr26_VLM_start()" >
<td width="20%">
<div class="one">
<div class="two" id='cvpr26_VLM_image'>
<img src="./files/cvpr26_VLM_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/cvpr26_VLM_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function cvpr26_VLM_start() {
document.getElementById('cvpr26_VLM_image').style.opacity = "1";
}
function cvpr26_VLM_stop() {
document.getElementById('cvpr26_VLM_image').style.opacity = "0";
}
cvpr26_VLM_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2507.18064">
    <papertitle_just>Adapting Large VLMs with Iterative and Manual Instructions for Generative Low-light Enhancement</papertitle_just>
  </a>
  <br>
  Xiaoran Sun<sup class="eq-contrib">*</sup>, Liyan Wang<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong><sup class="corr-lead">‡</sup>, Kin-man Lam, Zhixun Su<sup class="corr-lead">†</sup>, Yang Yang, Jinshan Pan, Cong Wang
  <br>
  <em>IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Findings</em>, 2026, Denver, USA<br>
<a href="https://arxiv.org/abs/2507.18064">arXiv</a> |
<a href="https://github.com/sunxiaoran01/VLM-IMI"><img src="https://img.shields.io/github/stars/sunxiaoran01/VLM-IMI?style=social&cacheSeconds=86400"></a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper UniFit -->
<tr data-category="gen-vision" data-role="eq-contrib" onmouseout="aaai26_UniFit_stop()" onmouseover="aaai26_UniFit_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'aaai26_UniFit_image'>
<img src="./files/aaai26_UniFit_after.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/aaai26_UniFit_before.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function aaai26_UniFit_start() {
document.getElementById('aaai26_UniFit_image').style.opacity = "1";
}
function aaai26_UniFit_stop() {
document.getElementById('aaai26_UniFit_image').style.opacity = "0";
}
aaai26_UniFit_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2511.15831">
    <papertitle_just>UniFit: Towards Universal Virtual Try-on with MLLM-Guided Semantic Alignment</papertitle_just>     
  </a>
  <br>
  Wei Zhang<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong><sup class="eq-contrib">*</sup>, Xin Li, Yan Zhang, Xiaofeng Cong, Cong Wang, Fengcai Qiao, Zhichao Lian<sup class="corr-lead">†</sup>
  <br>
<em>Association for the Advancement of Artificial Intelligence (AAAI)</em>, 2026, Singapore <br>
<a href="https://arxiv.org/abs/2511.15831">arXiv</a>
|
<a href="https://github.com/zwplus/UniFit"><img src="https://img.shields.io/github/stars/zwplus/UniFit?style=social&cacheSeconds=86400"></a>
| 
<a href="./files/aaai26_UniFit_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper MMGT -->
<tr data-category="gen-vision" onmouseout="tcsvt25_MMGT_stop()" onmouseover="tcsvt25_MMGT_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'tcsvt25_MMGT_image'>
<img src="./files/tcsvt25_MMGT_after.gif" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;"></div>
<img src="./files/tcsvt25_MMGT_before.gif" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
<script type="text/javascript">
function tcsvt25_MMGT_start() {
document.getElementById('tcsvt25_MMGT_image').style.opacity = "1";
}
function tcsvt25_MMGT_stop() {
document.getElementById('tcsvt25_MMGT_image').style.opacity = "0";
}
tcsvt25_MMGT_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2505.23120">
    <papertitle_just>MMGT: Motion Mask Guided Two-Stage Network for Co-Speech Gesture Video Generation</papertitle_just>     
  </a>
  <br>
  Siyuan Wang<sup class="eq-contrib">*</sup>, Jiawei Liu<sup class="eq-contrib">*</sup>, Wei Wang<sup class="corr-lead">†</sup>, <strong>Yeying Jin</strong>, Jinsong Du, Zhi Han
  <br>
<em>IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)</em>, 2025 <br>
<a href="https://arxiv.org/abs/2505.23120">arXiv</a>
|
<a href="https://github.com/SIA-IDE/MMGT"><img src="https://img.shields.io/github/stars/SIA-IDE/MMGT?style=social&cacheSeconds=86400"></a> 
| 
<a href="./files/tcsvt25_MMGT_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->


<!-- Paper 23 PosterCraft -->
<tr data-category="agentic-vlm" onmouseout="arxiv25_PosterCraft_stop()" onmouseover="arxiv25_PosterCraft_start()" >
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
  Sixiang Chen<sup class="eq-contrib">*</sup>, Jianyu Lai<sup class="eq-contrib">*</sup>, Jialin Gao<sup class="eq-contrib">*</sup>, Tian Ye, Haoyu Chen, Hengyu Shi, Shitong Shao, Yunlong Lin, Song Fei, Zhaohu Xing, <strong>Yeying Jin</strong>, Junfeng Luo, Xiaoming Wei, Lei Zhu<sup class="corr-lead">†</sup>
  <br>
<em>The International Conference on Learning Representations (ICLR)</em>, 2026, Rio, Brazil <br>
<a href="https://arxiv.org/abs/2506.10741">arXiv</a>
|
<a href="https://github.com/Ephemeral182/PosterCraft"><img src="https://img.shields.io/github/stars/Ephemeral182/PosterCraft?style=social&cacheSeconds=86400"></a>
| 
<a href="./files/arxiv25_PosterCraft_bibtex.txt">bibtex</a>
|
<a href="https://ephemeral182.github.io/PosterCraft/">Project Page</a>  
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
<tr data-category="gen-vision" onmouseout="acm25_DSDNet_stop()" onmouseover="acm25_DSDNet_start()" >
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
  Qirui Yang<sup class="eq-contrib">*</sup>, Fangpu Zhang<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong>, Qihua Cheng, Pengtao Jiang, Huanjing Yue<sup class="corr-lead">†</sup>, Jingyu Yang<sup class="corr-lead">†</sup>
  <br>
<em>ACM Multimedia (ACM'MM)</em>, 2025, Dublin, Ireland <br>
<a href="https://arxiv.org/abs/2504.15756">arXiv</a>
|
<a href="https://github.com/xxxxxxxxDSDNet/DSDNet-official"><img src="https://img.shields.io/github/stars/xxxxxxxxDSDNet/DSDNet-official?style=social&cacheSeconds=86400"></a>
|
<a href="./files/acm25_DSDNet_bibtex.txt">bibtex</a> 
|
<a href="https://xxxxxxxxdsdnet.github.io/DSDNet/">Project Page</a>  
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper Security: Adversarial Attacks -->
<tr data-category="security" data-role="eq-contrib" >
<td width="20%">
<div class="one">
<img src="./files/pr25_Attacks.png" style="width: 100%; aspect-ratio: 1 / 1; object-fit: cover;">
</div>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2504.17457">
    <papertitle_just>Unveiling Hidden Vulnerabilities in Digital Human Generation via Adversarial Attacks</papertitle_just>     
  </a>
  <br>
  Zhiying Li<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong><sup class="eq-contrib">*</sup>, Fan Shen, Zhi Liu, Weibin Chen, Pengju Zhang, Xiaomei Zhang, Boyu Chen, Michael Shen, Kejian Wu, Zhaoxin Fan<sup class="corr-lead">†</sup>, Jin Dong<sup class="corr-lead">†</sup>
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
<tr data-category="gen-vision" onmouseout="iccv25_GenHaze_stop()" onmouseover="iccv25_GenHaze_start()" >
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
  <a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_GenHaze_Pioneering_Controllable_One-Step_Realistic_Haze_Generation_for_Real-World_Dehazing_ICCV_2025_paper.pdf">
    <papertitle_just>GenHaze: Pioneering Controllable One-Step Realistic Haze Generation for Real-World Dehazing</papertitle_just>     
  </a>
  <br>
 Sixiang Chen, Tian Ye, Yunlong Lin, <strong>Yeying Jin</strong>, Yijun Yang, Haoyu Chen, Jianyu Lai, Song Fei, Zhaohu Xing, Fugee Tsung, Lei Zhu<sup class="corr-lead">†</sup>
  <br>
<em>International Conference on Computer Vision (ICCV)</em>, 2025, Hawaii, USA <br>
<a href="https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_GenHaze_Pioneering_Controllable_One-Step_Realistic_Haze_Generation_for_Real-World_Dehazing_ICCV_2025_paper.pdf">arXiv</a>
| 
<a href="./files/iccv25_GenHaze_bibtex.txt">bibtex</a>  
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->


<!-- ###################################################################################################-->
<!-- Paper 19 JarvisIR -->
<tr data-category="agentic-vlm" onmouseout="cvpr25_JarvisIR_stop()" onmouseover="cvpr25_JarvisIR_start()" >
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
  Yunlong Lin<sup class="eq-contrib">*</sup>, Zixu Lin<sup class="eq-contrib">*</sup>, Haoyu Chen<sup class="eq-contrib">*</sup>, Panwang Pan<sup class="eq-contrib">*</sup>, Chenxin Li, Sixiang Chen, Kairun Wen, <strong>Yeying Jin</strong>, Wenbo Li<sup class="corr-lead">†</sup>, Xinghao Ding<sup class="corr-lead">†</sup>
  <br>
<em>Computer Vision and Pattern Recognition (CVPR)</em>, 2025, Nashville, USA <br>
<a href="https://arxiv.org/abs/2504.04158">arXiv</a>
|
<a href="https://github.com/LYL1015/JarvisIR"><img src="https://img.shields.io/github/stars/LYL1015/JarvisIR?style=social&cacheSeconds=86400"></a>
| 
<a href="./files/cvpr25_JarvisIR_bibtex.txt">bibtex</a>
|
<a href="https://cvpr2025-jarvisir.github.io/">Project Page</a>  
|
<a href="https://huggingface.co/spaces/LYL1015/JarvisIR">online demo</a>  
|
<a href="https://mp.weixin.qq.com/s/zYhqjMfThwwTK9nhXwYu4g">link</a>    
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper LoViF 2026 Challenge -->
<tr data-category="workshop" data-role="corr-author" onmouseout="cvpr26_lovif_stop()" onmouseover="cvpr26_lovif_start()" >
<td width="20%">
<div class="one">
<div class="two" id='cvpr26_lovif_image'><img src='./files/cvpr26_LoViF_after.png' style="width:100%;aspect-ratio:1/1;object-fit:cover;"></div>
<img src='./files/cvpr26_LoViF_before.png' style="width:100%;aspect-ratio:1/1;object-fit:cover;">
</div>
<script type="text/javascript">
function cvpr26_lovif_start() {
document.getElementById('cvpr26_lovif_image').style.opacity = "1";
}
function cvpr26_lovif_stop() {
document.getElementById('cvpr26_lovif_image').style.opacity = "0";
}
cvpr26_lovif_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2604.10655">
    <papertitle_just>LoViF 2026: The First Challenge on Weather Removal in Videos</papertitle_just>
  </a>
  <br>
  Chenghao Qian, Xin Li, <strong>Yeying Jin</strong><sup class="corr-lead">†</sup>, Shangguan Sun, Yilian Zhong, etc. <span style="color:#888;font-size:0.92em;">(Organizer & Corresponding Author)</span>
  <br>
  <em>Computer Vision and Pattern Recognition (CVPR)</em>, 2026, Denver, USA <br>
  <a href="https://arxiv.org/abs/2604.10655">arXiv</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper NTIRE 2026 -->
<tr data-category="workshop" data-role="corr-author" onmouseout="ntire26_rd_stop()" onmouseover="ntire26_rd_start()" >
<td width="20%">
<div class="one">
<div class="two" id='ntire26_rd_image'><img src='./files/ntire26_raindropclarify_after.png'></div>
<img src='./files/ntire26_raindropclarify_before.png'>
</div>
<script type="text/javascript">
function ntire26_rd_start() {
document.getElementById('ntire26_rd_image').style.opacity = "1";
}
function ntire26_rd_stop() {
document.getElementById('ntire26_rd_image').style.opacity = "0";
}
ntire26_rd_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2604.10634">
    <papertitle_just>NTIRE 2026 The Second Challenge on Day and Night Raindrop Removal for Dual-Focused Images: Methods and Results</papertitle_just>
  </a>
  <br>
  Xin Li, <strong>Yeying Jin</strong><sup class="corr-lead">†</sup>, Suhang Yao, etc. <span style="color:#888;font-size:0.92em;">(Organizer & Corresponding Author)</span>
  <br>
  <em>Computer Vision and Pattern Recognition (CVPR)</em>, 2026, Denver, USA <br>
  <a href="https://arxiv.org/abs/2604.10634">arXiv</a>
  |
  <a href="https://github.com/jinyeying/RaindropClarity"><img src="https://img.shields.io/github/stars/jinyeying/RaindropClarity?style=social&cacheSeconds=3600"></a>
  |
  <a href="https://www.codabench.org/competitions/12808/">competition</a>
  |
  <a href="https://lixinustc.github.io/CVPR-NTIRE2026-RainDrop-Competition.github.io/">challenge</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 18 ntire -->
<tr data-category="workshop" data-role="corr-author" onmouseout="ntire25_rd_stop()" onmouseover="ntire25_rd_start()" >
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
    <papertitle_just>NTIRE 2025 Challenge on Day and Night Raindrop Removal for Dual-focused Images: Methods and Results</papertitle_just>
  </a>
  <br>
  Xin Li, <strong>Yeying Jin</strong><sup class="corr-lead">†</sup>, Xin Jin, etc. <span style="color:#888;font-size:0.92em;">(Organizer & Corresponding Author)</span>
  <br>
  <em>Computer Vision and Pattern Recognition (CVPR)</em>, 2025, Nashville, USA <br>
  <a href="https://arxiv.org/abs/2504.12711">arXiv</a>
  |
  <a href="https://github.com/jinyeying/RaindropClarity"><img src="https://img.shields.io/github/stars/jinyeying/RaindropClarity?style=social&cacheSeconds=3600"></a>
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
<tr data-category="gen-vision" data-role="first-author" onmouseout="eccv24_rd_stop()" onmouseover="eccv24_rd_start()" >  
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
  <a href="https://github.com/jinyeying/RaindropClarity"><img src="https://img.shields.io/github/stars/jinyeying/RaindropClarity?style=social&cacheSeconds=3600"></a>
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
<tr data-category="multimodal" onmouseout="acl25_hscr_stop()" onmouseover="acl25_hscr_start()" >
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
  Songtao Jiang, Yan Zhang, <strong>Yeying Jin</strong>, Zhihang Tang, Yangyang Wu, Yang Feng, Jian Wu, Zuozhu Liu<sup class="corr-lead">†</sup>
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
<tr data-category="multimodal" onmouseout="acl25_vqa_stop()" onmouseover="acl25_vqa_start()" >
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
  Songtao Jiang<sup class="eq-contrib">*</sup>, Chenyi Zhou<sup class="eq-contrib">*</sup>, Yan Zhang, <strong>Yeying Jin</strong>, Zuozhu Liu<sup class="corr-lead">†</sup>
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
<tr data-category="multimodal" onmouseout="arxiv24_dpo_stop()" onmouseover="arxiv24_dpo_start()" >
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
  Songtao Jiang, Yan Zhang, Ruizhe Chen, <strong>Yeying Jin</strong>, Zuozhu Liu<sup class="corr-lead">†</sup>
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
<tr data-category="multimodal" onmouseout="arxiv24_CGSAM_stop()" onmouseover="arxiv24_CGSAM_start()" >
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
  Songtao Jiang<sup class="eq-contrib">*</sup>, Yan Zhang<sup class="eq-contrib">*</sup>, Chenyi Zhou, <strong>Yeying Jin</strong>, Yang Feng, Jian Wu, Zuozhu Liu<sup class="corr-lead">†</sup>
  <br>
  <em>ADHIP Best Paper Award</em>, 2024, Jiaxing, China <br>
  <a href="https://arxiv.org/abs/2404.04514">arXiv</a>
  |
  <a href="https://github.com/jiangsongtao/VTprompt"><img src="https://img.shields.io/github/stars/jiangsongtao/VTprompt?style=social&cacheSeconds=86400"></a>
  |
  <a href="./files/CGSAM24_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 12 Med-MoE -->
<tr data-category="multimodal" onmouseout="emnlp24_moe_stop()" onmouseover="emnlp24_moe_start()" >
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
  Songtao Jiang<sup class="eq-contrib">*</sup>, Tuo Zheng<sup class="eq-contrib">*</sup>, Yan Zhang, <strong>Yeying Jin</strong>, Li Yuan, Zuozhu Liu<sup class="corr-lead">†</sup>
  <br>
  <em>EMNLP finding</em>, 2024, Miami, Florida <br>
  <a href="https://arxiv.org/abs/2404.10237">arXiv</a>
  |
  <a href="https://github.com/jiangsongtao/Med-MoE"><img src="https://img.shields.io/github/stars/jiangsongtao/Med-MoE?style=social&cacheSeconds=86400"></a>
  |
  <a href="./files/emnlp24_moe_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 11 Dualrain -->
<tr data-category="gen-vision" data-role="eq-contrib" onmouseout="eccv24_dualrain_stop()" onmouseover="eccv24_dualrain_start()" >
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
eccv24_dualrain_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08521.pdf">
    <papertitle_just>Dual-Rain: Video Rain Removal using Assertive and Gentle Teachers</papertitle_just>     
  </a>
  <br>
  Tingting Chen<sup class="eq-contrib">*</sup>, Beibei Lin<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong><sup class="eq-contrib">*</sup>, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan
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
<tr data-category="gen-vision" onmouseout="eccv24_sr_stop()" onmouseover="eccv24_sr_start()" >
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
  Xin Li<sup class="eq-contrib">*</sup>, Bingchen Li<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong>, Cuiling Lan, Hanxin Zhu, Yulin Ren, Zhibo Chen<sup class="corr-lead">†</sup>
  <br>
<em>European Conference on Computer Vision (ECCV)</em>, 2024, Milan, Italy <br>
<a href="https://arxiv.org/abs/2407.13108">arXiv</a>
|
<a href="https://github.com/lixinustc/UCIP_MLP_source_code/tree/main"><img src="https://img.shields.io/github/stars/lixinustc/UCIP_MLP_source_code?style=social&cacheSeconds=86400"></a>
|
<a href="./files/eccv24_ucip_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 9 NightHaze -->
<tr data-category="gen-vision" data-role="eq-contrib" onmouseout="submit24_nighthaze_stop()" onmouseover="submit24_nighthaze_start()" >
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
  Beibei Lin<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong><sup class="eq-contrib">*</sup>, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan
  <br>
<em>Association for the Advancement of Artificial Intelligence (AAAI)</em>, 2025, Philadelphia, USA <br>
<a href="https://arxiv.org/abs/2403.07408">arXiv</a>
|
<a href="https://github.com/bb12346/nighthaze_codes"><img src="https://img.shields.io/github/stars/bb12346/nighthaze_codes?style=social&cacheSeconds=86400"></a> 
|
<a href="./files/submit24_nighthaze_bibtex.txt">bibtex</a> 
|
<a href="https://bb12346.github.io/NightHaze/">Project Page</a>  
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 8 Super-resolution -->
<tr data-category="gen-vision" onmouseout="cvpr24_sr_stop()" onmouseover="cvpr24_sr_start()" >
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
  Bingchen Li<sup class="eq-contrib">*</sup>, Xin Li<sup class="eq-contrib">*</sup>, Hanxin Zhu, <strong>Yeying Jin</strong>, Ruoyu Feng, Zhizheng Zhang, Zhibo Chen<sup class="corr-lead">†</sup>
  <br>
<em>Conference on Computer Vision and Pattern Recognition (CVPR)</em>, 2024, Seattle, USA <br>
<a href="https://arxiv.org/abs/2402.19387">arXiv</a>
|
<a href="https://github.com/lbc12345/SeD"><img src="https://img.shields.io/github/stars/lbc12345/SeD?style=social&cacheSeconds=86400"></a>
|
<a href="./files/cvpr24_sr_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 7 DeS3 -->
<tr data-category="gen-vision" data-role="first-author" onmouseout="aaai24_des3_stop()" onmouseover="aaai24_des3_start()" >
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
<a href="https://github.com/jinyeying/DeS3_Deshadow"><img src="https://img.shields.io/github/stars/jinyeying/DeS3_Deshadow?style=social&cacheSeconds=86400"></a>
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
<tr data-category="gen-vision" data-role="eq-contrib" onmouseout="aaai24_nightrain_stop()" onmouseover="aaai24_nightrain_start()" >
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
  Beibei Lin<sup class="eq-contrib">*</sup>, <strong>Yeying Jin</strong><sup class="eq-contrib">*</sup>, Wending Yan, Wei Ye, Yuan Yuan, Sunli Zhang, Robby T. Tan
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
<tr data-category="gen-vision" data-role="first-author" onmouseout="eccv22_nightenhance_stop()" onmouseover="eccv22_nightenhance_start()" >
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
<a href="https://github.com/jinyeying/night-enhancement"><img src="https://img.shields.io/github/stars/jinyeying/night-enhancement?style=social&cacheSeconds=86400"></a>
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
<tr data-category="gen-vision" data-role="first-author" onmouseout="iccv21_dcshadownet_stop()" onmouseover="iccv21_dcshadownet_start()" >
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
<a href="https://github.com/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal"><img src="https://img.shields.io/github/stars/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal?style=social&cacheSeconds=86400"></a>
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
<tr data-category="gen-vision" data-role="first-author eq-contrib" onmouseout="acmmm23_nightdehaze_stop()" onmouseover="acmmm23_nightdehaze_start()" >
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
  <strong>Yeying Jin</strong><sup class="eq-contrib">*</sup>, Beibei Lin<sup class="eq-contrib">*</sup>, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan
  <br>
<em>ACM Multimedia (ACM'MM)</em>, 2023, Ottawa, Canada <br>
<a href="https://arxiv.org/abs/2308.01738">arXiv</a>
|
<a href="https://github.com/jinyeying/nighttime_dehaze"><img src="https://img.shields.io/github/stars/jinyeying/nighttime_dehaze?style=social&cacheSeconds=86400"></a>
|
<a href="./files/acmmm23_nightdehaze_bibtex.txt">bibtex</a>
|
<a href="https://dl.acm.org/doi/10.1145/3581783.3611884">paper</a>
|  
<a href="https://www.dropbox.com/scl/fi/2wo8q4y2la58a3f2kvum0/0859_poster.pdf?rlkey=7x8jbdh0o550r8pvzqugt4szs&dl=0">poster</a>
|
<a href="https://www.dropbox.com/scl/fi/z0jn6qvr1yo8snlctg67g/0859_slides.pdf?rlkey=5g9j15xz180ayw8u3f0rwb6d2&st=y78ih372&dl=0">slides</a>
| 
<a href="https://www.dropbox.com/sh/7qzmb3y9akejape/AABYf2ZAqn_5vmPsOPg7KqoMa?dl=0">data</a>  
<p></p>
<p>First learning-based network handling nighttime haze and glow using APSF.</p>
</td>
</tr>
<!-- ###################################################################################################-->
  
<!-- ###################################################################################################-->
<!-- Paper 2 Reflectance, AAAI'23 -->
<tr data-category="gen-vision" data-role="first-author" onmouseout="aaai23_reflectance_stop()" onmouseover="aaai23_reflectance_start()" >
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
<a href="https://github.com/jinyeying/S-Aware-network"><img src="https://img.shields.io/github/stars/jinyeying/S-Aware-network?style=social&cacheSeconds=86400"></a>
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
<tr data-category="gen-vision" data-role="first-author" onmouseout="accv22_defog_stop()" onmouseover="accv22_defog_start()" >
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
<a href="https://github.com/jinyeying/FogRemoval"><img src="https://img.shields.io/github/stars/jinyeying/FogRemoval?style=social&cacheSeconds=86400"></a>
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

# 💬 Organizer {#organizer}
<style>
  .talks-table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
    font-size: 0.88em;
    line-height: 1.35;
  }
  .talks-table th {
    background: #f5f6fa;
    padding: 5px 4px;
    text-align: left;
    font-size: 0.85em;
    letter-spacing: 0.02em;
    white-space: nowrap;
  }
  .talks-table td {
    padding: 4px 4px;
    vertical-align: top;
    border-bottom: 1px solid #f0f0f0;
  }
  .talks-table td:last-child {
    color: #667085;
    font-size: 0.88em;
    line-height: 1.4;
  }
  .talks-table tr:hover td { background: #fafbff; }
</style>
<table class="talks-table">
  <colgroup>
    <col style="width:24%">
    <col style="width:62%">
    <col style="width:14%">
  </colgroup>
  <tr>
    <th>Workshop</th>
    <th>Title</th>
    <th>Date & Venue</th>
  </tr>

  <tr>
    <td><a href="https://lovif-eccv2026-workshop.github.io/" target="_blank">ECCV 2026 LoViF Workshop</a></td>
    <td><a href="https://lovif-eccv2026-workshop.github.io/" target="_blank">The 2nd Workshop on Low‑Level Vision Frontiers (Generative AI, Preference Optimization, and Agentic Systems)</a></td>
    <td>09.2026<br>Malmö, Sweden</td>
  </tr>

  <tr>
    <td><a href="https://lovif-cvpr2026-workshop.github.io/" target="_blank">CVPR 2026 LoViF Workshop</a></td>
    <td><a href="https://lovif-cvpr2026-workshop.github.io/" target="_blank">The 1st Workshop on Low‑Level Vision Frontiers (Generative AI, Preference Optimization, and Agentic Systems)</a></td>
    <td>06.04.2026@504<br>Denver, USA</td>
  </tr>

  <tr>
    <td><a href="https://agentic-visual-media.insait.ai/" target="_blank">CVPR 2026 AGENTIC Workshop</a></td>
    <td><a href="https://agentic-visual-media.insait.ai/" target="_blank">Workshop on Agentic AI for Visual Media</a></td>
    <td>06.03.2026@1EF<br>Denver, USA</td>
  </tr>

  <tr>
    <td><a href="https://urvis-workshop.github.io/" target="_blank">CVPR 2026 URVIS Workshop</a></td>
    <td><a href="https://urvis-workshop.github.io/" target="_blank">Unified Robotic Vision with Cross-Modal Sensing and Alignment</a></td>
    <td>06.04.2026@4AB<br>Denver, USA</td>
  </tr>

  <tr>
    <td><a href="https://ai4streaming-workshop.github.io/" target="_blank">CVPR 2026 AIGENS Workshop</a></td>
    <td><a href="https://ai4streaming-workshop.github.io/" target="_blank">The 3rd Workshop on AI for Content Generation, Quality Enhancement and Streaming</a></td>
    <td>06.03.2026@105<br>Denver, USA</td>
  </tr>

  <tr>
    <td><a href="https://www.codabench.org/competitions/12808/" target="_blank">CVPR 2026 NTIRE Challenge</a></td>
    <td><a href="https://lixinustc.github.io/CVPR-NTIRE2026-RainDrop-Competition.github.io/" target="_blank">The 2nd Challenge on Day and Night Raindrop Removal for Dual-Focused Images</a></td>
    <td>06.04.2026@504<br>Denver, USA</td>
  </tr>

  <tr>
    <td><a href="https://aaai.org/conference/aaai/aaai-26/tutorial-and-lab-list/" target="_blank">AAAI 2026 Workshop</a></td>
    <td><a href="https://lixinustc.github.io/GenAI-Agents-for-Low-level-Vision.github.io/" target="_blank">The Application of Generative AI and Intelligent Agents in Low-level Vision</a></td>
    <td>01.2026<br>Singapore</td>
  </tr>

  <tr>
    <td><a href="https://codalab.lisn.upsaclay.fr/competitions/21345" target="_blank">CVPR 2025 NTIRE Challenge</a></td>
    <td><a href="https://lixinustc.github.io/CVPR-NTIRE2025-RainDrop-Competition.github.io" target="_blank">The 1st Challenge on Day and Night Raindrop Removal for Dual-Focused Images</a></td>
    <td>06.2025<br>Nashville, USA</td>
  </tr>
</table>

# 🎤 Invited Talks {#invited-talks}
<div class="pub-filters">
  <button class="pub-filter-btn talk-filter-btn active" data-cat="all" onclick="filterTalks('all')">All</button>
  <button class="pub-filter-btn talk-filter-btn" data-cat="world-model" onclick="filterTalks('world-model')">World Model</button>
  <button class="pub-filter-btn talk-filter-btn" data-cat="gen-vision" onclick="filterTalks('gen-vision')">Generation & Vision</button>
</div>
<script>
function filterTalks(cat) {
  document.querySelectorAll('#talks-main-table tr:not(:first-child)').forEach(function(tr) {
    if (cat === 'all') tr.style.display = '';
    else if (cat === 'world-model') tr.style.display = tr.getAttribute('data-talk-cat') === 'world-model' ? '' : 'none';
    else tr.style.display = tr.getAttribute('data-talk-cat') !== 'world-model' ? '' : 'none';
  });
  document.querySelectorAll('.talk-filter-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.cat === cat);
  });
}
</script>
<table class="talks-table" id="talks-main-table">
  <colgroup>
    <col style="width:33%">
    <col style="width:53%">
    <col style="width:14%">
  </colgroup>
  <tr>
    <th>Host</th>
    <th>Topic</th>
    <th>Date & Venue</th>
  </tr>

 <tr data-talk-cat="world-model">
    <td><a href="https://www.jiqizhixin.com/">CVPR 机器之心</a></td>
    <td>Invited Talk (w/ <a href="https://liuziwei7.github.io/">Ziwei Liu</a> (NTU), <a href="https://sites.google.com/view/showlab">Mike Zheng Shou</a> (NUS), <a href="https://ruoshiliu.github.io/">Ruoshi Liu</a> (UMD))</td>
    <td>06.06.2026<br>Denver, USA</td>
 </tr>

 <tr data-talk-cat="world-model">
    <td><a href="https://urvis-workshop.github.io/">CVPR URVIS</a> (invited by <a href="https://sites.google.com/view/zwwu/accueil">Zongwei Wu</a>)</td>
    <td>World Model</td>
    <td>06.04.2026@4AB<br>Denver, USA</td>
 </tr>

 <tr data-talk-cat="world-model">
    <td><a href="https://ai4streaming-workshop.github.io/">CVPR AIGENS</a> (invited by <a href="https://mv-lab.github.io/">Marcos V. Conde</a>)</td>
    <td>Game World Model for Video Generation</td>
    <td>06.03.2026@105<br>Denver, USA</td>
 </tr>

 <tr data-talk-cat="world-model">
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"> SPARK Share</td>
    <td>From Video Generation to World Model</td>
    <td>05.22.2026<br>Singapore</td>
 </tr>

 <tr data-talk-cat="world-model">
    <td><a href="https://singaporevisionday.github.io/svd2026/">Singapore Vision Day</a> (invited by <a href="https://www.comp.nus.edu.sg/~leegh/">Gim Hee Lee</a>)</td>
    <td><a href="https://singaporevisionday.github.io/svd2026/">Game World Model</a><br>World Model Panel Discussion (w/ <a href="https://v3alab.github.io/#about">Qi Wu</a> (U Adelaide), <a href="https://www.3dunderstanding.org/">Angela Dai</a> (TUM), <a href="https://xingangpan.github.io/">Xingang Pan</a> (NTU))</td>
    <td>05.16.2026<br>Singapore</td>
 </tr>

 <tr data-talk-cat="world-model">
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"> ICLR Booth Talk<br><img src="/files/tencent.png" alt="Tencent" width="85" height="20"> Game Session Talk</td>
    <td><a href="https://www.linkedin.com/posts/jinyeying_iclr-2026-sharing-our-work-on-world-activity-7454451566251765760-pHR1?utm_source=share&utm_medium=member_desktop&rcm=ACoAACNosSgBI_KUO4Duouy2mfHXSwk8Ap0YHFE">From AIGC to World Model</a></td>
    <td>04.25.2026<br>Rio, Brazil</td>
 </tr>

 <tr data-talk-cat="world-model">
    <td>NUS EE6934 Emerging Topics in AI and Deep Learning Guest Lecture (invited by <a href="https://sites.google.com/site/sitexinchaowang/">Xinchao Wang</a>)</td>
    <td>From AIGC to World Model</td>
    <td>03.17.2026<br>Singapore</td>
 </tr>

 <tr>
    <td>AAAI (invited by <a href="https://lixinustc.github.io/">Xin Li</a>)</td>
    <td><a href="https://lixinustc.github.io/GenAI-Agents-for-Low-level-Vision.github.io/">From Creation to Perception: Generative AI for Content Generation</a></td>
    <td>01.2026<br>Singapore</td>
 </tr>

 <tr>
    <td>Low-level Community (invited by <a href="https://cschenxiang.github.io/">Xiang Chen</a>)</td>
    <td><a href="https://mp.weixin.qq.com/s/4hsDsLlJG-JAacAwvlm4XA">AIGC-Powered Game Marketing: From Generation to Deployment</a></td>
    <td>01.2026<br>Singapore</td>
 </tr>

 <tr>
    <td><a href="https://ai4streaming-workshop.github.io/">ICCV AIGENS</a> (invited by <a href="https://mv-lab.github.io/">Marcos V. Conde</a>)</td>
    <td><a href="https://ai4streaming-workshop.github.io/">From Creation to Perception: Generative AI for Content Generation</a></td>
    <td>10.2025<br>Hawaii, USA</td>
 </tr>

 <tr>
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"> Programmers Video</td>
    <td>Exploring SORA: Unlocking the Core of AI Video Creation
      [<a href="https://www.bilibili.com/video/BV1Ymy7BJEmy/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292" target="_blank">Video</a>]</td>
    <td>11.2025<br>Singapore</td>
 </tr>

  <tr>
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"></td>
    <td>AI Video Gen | When Wukong meets Yayoi Kusama</td>
    <td>05.2025<br>Singapore</td>
  </tr>

  <tr>
    <td>ICLR (invited by <a href="https://qhlin.me/">Kevin QH. Lin</a>)</td>
    <td><a href="https://showlab.github.io/omg/">AI × Gaming: Creative Applications of AIGC</a>
      [<a href="https://www.bilibili.com/video/BV1dzJfzbEmh/?share_source=copy_web&vd_source=2da049ce4677af057256ebc4a00a8292" target="_blank">Video</a>]</td>
    <td>04.2025<br>Singapore</td>
  </tr>

  <tr>
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"></td>
    <td>AI Generation: Inspiring Game Marketing and Development</td>
    <td>02.2025<br>Singapore</td>
  </tr>

  <tr>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td><a href="https://www.bilibili.com/video/BV1p5bFevEgP/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Raindrop Clarity: Dual-Focused, Day and Night</a></td>
    <td>09.2024</td>
  </tr>

  <tr>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td><a href="https://www.bilibili.com/video/BV1wc411v7zf/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Shadow Removal using Diffusion Model</a></td>
    <td>01.2024</td>
  </tr>

  <tr>
    <td><img src="/files/tencent.png" alt="Tencent" width="85" height="20"></td>
    <td>Applications of Generative AI</td>
    <td>11.2023<br>Singapore</td>
  </tr>

  <tr>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei</td>
    <td>Visibility Enhancement using Generative Model</td>
    <td>07.2023</td>
  </tr>

  <tr>
    <td><img src="/files/adobe.png" alt="Adobe" width="20" height="20"> Adobe (invited by <a href="https://www.erickee.com/">Eric Kee</a>)</td>
    <td>NextCam Reading Group: Light-effects Suppression</td>
    <td>07.2023<br>USA</td>
  </tr>

  <tr>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei</td>
    <td>Image/Video Restoration and Generation</td>
    <td>03.2023</td>
  </tr>

  <tr>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td><a href="https://www.bilibili.com/video/BV1Ca4y1C7xi/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Intrinsic Image Decomposition</a></td>
    <td>02.2023</td>
  </tr>

  <tr>
    <td><img src="/files/ByteDance.png" alt="ByteDance" width="100" height="20"> (invited by <a href="https://hanshuyan.github.io/">Hanshu Yan</a>)</td>
    <td>Diffusion Model in Image Processing</td>
    <td>01.2023</td>
  </tr>

  <tr>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei</td>
    <td>Visibility Enhancement in Nighttime</td>
    <td>12.2022<br>Singapore</td>
  </tr>

  <tr>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td><a href="https://www.bilibili.com/video/BV1Ec411s7at/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Unsupervised Image Restoration and Generation</a></td>
    <td>11.2022</td>
  </tr>

</table>

<table class="talks-table" style="margin-top:6px;">
  <colgroup>
    <col style="width:68%">
    <col style="width:32%">
  </colgroup>
  <tr>
    <th>Presented at</th>
    <th>Date & Venue</th>
  </tr>
  <tr>
    <td><img src="/files/VALSE.png" alt="VALSE" width="23.2" height="20"> <a href="https://valser.org/2024/#/poster">VALSE</a></td>
    <td>05.2024, Chongqing, China</td>
  </tr>
  <tr>
    <td><img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> <a href="https://www.comp.nus.edu.sg/~leegh/svd/">Singapore Vision Day</a></td>
    <td>05.2023, Singapore</td>
  </tr>
  <tr>
    <td><img src="/files/aisg.png" alt="AISG" width="20" height="20"> <a href="https://aisingapore.org/ai-governance/aisg-ai-governance-research-symposium-2023/">AI Research Symposium</a></td>
    <td>01.2023, Singapore</td>
  </tr>
</table>

# ✍️ Blogs {#blogs}
<div class="pub-filters" id="blog-topic-filters">
  <button class="pub-filter-btn blog-filter-btn active" data-cat="all" onclick="filterBlogs('all')">All</button>
  <button class="pub-filter-btn blog-filter-btn" data-cat="world-model" onclick="filterBlogs('world-model')">World Model</button>
  <button class="pub-filter-btn blog-filter-btn" data-cat="gen-vision" onclick="filterBlogs('gen-vision')">Generation & Vision</button>
</div>
<script>
function filterBlogs(cat) {
  document.querySelectorAll('tr.blog-row').forEach(function(tr) {
    tr.style.display = (cat === 'all' || tr.getAttribute('data-blog-cat') === cat) ? '' : 'none';
  });
  document.querySelectorAll('.blog-filter-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.cat === cat);
  });
}
</script>
<table class="talks-table" id="blogs-table">
  <colgroup>
    <col style="width:78%">
    <col style="width:22%">
  </colgroup>
  <tr>
    <th>Title</th>
    <th>Date</th>
  </tr>
  <tr class="blog-row" data-blog-cat="world-model">
    <td><a href="https://zhuanlan.zhihu.com/p/2035741904558634682">一键创世，遥遥领先？快乐生蚝HappyOyster到底有多快乐</a></td>
    <td>04.2026</td>
  </tr>
  <tr class="blog-row" data-blog-cat="world-model">
    <td><a href="https://zhuanlan.zhihu.com/p/2027169068495456204">世界模型再添王炸，Marble 1.1一手测评来了！</a></td>
    <td>04.2026</td>
  </tr>
  <tr class="blog-row" data-blog-cat="world-model">
    <td><a href="https://zhuanlan.zhihu.com/p/2004490330423174448">AI视频的大结局？Seedance 2.0掀桌子了! 下一站在哪?</a></td>
    <td>02.2026</td>
  </tr>
  <tr class="blog-row" data-blog-cat="world-model">
    <td><a href="https://zhuanlan.zhihu.com/p/1957164727273784702">Sora2：视频生成一年半的变化与展望</a></td>
    <td>10.2025</td>
  </tr>
  <tr class="blog-row" data-blog-cat="world-model">
    <td><a href="https://zhuanlan.zhihu.com/p/686681635">Sora揭秘: OpenAI文生视频模型, Diffusion+Transformer带来的思考</a></td>
    <td>02.2024</td>
  </tr>
  <tr class="blog-row" data-blog-cat="gen-vision">
    <td><a href="https://zhuanlan.zhihu.com/p/1925607245346996265">AI赋能UGC | 点亮每一位玩家的英雄梦</a></td>
    <td>2025</td>
  </tr>
  <tr class="blog-row" data-blog-cat="gen-vision">
    <td><a href="https://zhuanlan.zhihu.com/p/24492948611">CVPR 2025 NTIRE赛事 | 首届多场景雨滴去除挑战赛</a></td>
    <td>06.2025</td>
  </tr>
  <tr class="blog-row" data-blog-cat="gen-vision">
    <td><a href="https://zhuanlan.zhihu.com/p/595440529">ECCV 2022 | 夜间图像增强: 层分解遇到光效应抑制网络</a></td>
    <td>10.2022</td>
  </tr>
</table>

# 🏫 Education {#education}
- 01.2020-01.2024: Ph.D. (AI and Deep Learning), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore (CAP: 4.75/5.00)
- 08.2017-08.2018: M.S. (Electrical and Computer Engineering), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore
- 09.2013-07.2017: B.Eng (Electrical and Computer Engineering), <img src="/files/UESTC.png" alt="UESTC" width="20.842" height="20"> UESTC, China (GPA: 3.93/4.00)

# 👔 Internship and Work Experience {#work}
- 11.2023-Present: Staff Researcher at <img src="/files/tencent.png" alt="Tencent" width="85" height="20"> Singapore.
- 06.2023-09.2023: <img src="/files/adobe.png" alt="Adobe" width="20" height="20"> [Adobe Research Intern](https://www.adobe.com/), Creative Intelligence Lab, mentored by [Prof. Connelly Barnes](http://www.connellybarnes.com/work/), [Prof. Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), worked with [Yuqian Zhou](https://yzhouas.github.io/), [Lingzhi Zhang](https://owenzlz.github.io/), [Sohrab Amirghodsi](https://www.linkedin.com/in/sohrab-amirghodsi-a89548a3/), [Eric Kee](https://www.erickee.com/).
- 01.2019-01.2020: Machine Learning Researcher at <img src="/files/biomind.png" alt="Biomind" width="80" height="20"> Singapore, advised by [Prof. Jiashi Feng](https://sites.google.com/site/jshfeng/), worked on Biomedical Image Synthesis, Super-resolution, Tumor Segmentation and Classification, expo demo for ["Deep Learning-Based End-to-end Automatic Contouring and Automated Radiation Therapy Treatment Planning System"](https://media.neurips.cc/Conferences/NeurIPS2019/NeurIPS_Expo_Book_2019.pdf).

# 🎖 Honors and Awards {#awards}
- [“Yayoi Kusama × Wukong”](https://modelscope.cn/brand/view/game-wan?branch=0&tree=4), *ModelScope Wan 2.1 Video Generation Challenge* — 2nd Place  
- [Knowledge Award](https://zhuanlan.zhihu.com/p/686681635), [Excellent R&D Award](https://www.dropbox.com/scl/fi/h32jdvfrftrdls3rwjesi/Tencent_Excellent_R-D_Award.jpg?rlkey=xw5225oazo9kkoziuznsnhtpz&st=apklpn9u&dl=0), [Outstanding Mentor](https://www.dropbox.com/scl/fi/kcszrth49835tfvcirjot/Mentor.jpg?rlkey=mf4zo301alayou3tvr7yaedpk&st=je6i1qgd&dl=0), Outstanding Contributor 
- CVPR Student Mentor, Tencent Outstanding Mentor Award
- [AI Singapore (AISG) Ph.D. Fellowship](https://aisingapore.org/research/phd-fellowship-programme/) *(Singapore’s most prestigious Ph.D. scholarship)* — Theme: Continuous Learning AI, Self-supervised Learning

# 💻 Professional Services {#services}
- Journal Reviewer: TPAMI, IJCV, TIP, TNNLS, TMM, TCSVT, TVCJ, NEUCOM, CVIU, etc.
- Conference Reviewer: ICML (Gold Reviewer Award), NeurIPS, ICLR, CVPR, ICCV, ECCV, AAAI, ACM MM, ACL, MICCAI, ACCV, IJCAI, IJCNN, etc.
- Teaching Assistant: [EE5731 Visual Computing](https://tanrobby.github.io/teaching/ece_visual/index.html), EE5904 Neural Network (NUS ECE)
- NUS ECE Adjunct Faculty

<div style="padding-bottom: 60vh;"></div>




