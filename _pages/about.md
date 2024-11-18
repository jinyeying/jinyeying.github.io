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

I am a Senior Researcher at [Tencent](https://www.tencent.com/en-us/about.html). I earned my PhD degree from <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> [National University of Singapore (NUS), Department of Electrical and Computer Engineering (ECE)](https://cde.nus.edu.sg/ece/), supervised by [Prof. Robby T. Tan](http://tanrobby.github.io/). 
I had my research internship in <img src="/files/adobe.png" alt="Adobe" width="20" height="20"> [Adobe](https://research.adobe.com/), mentored by [Prof. Connelly Barnes](http://www.connellybarnes.com/work/).

Previously, I completed my M.Sc. degree at the <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> [National University of Singapore (NUS)](https://cde.nus.edu.sg/ece/); received my B.Eng. degree from the <img src="/files/UESTC.png" alt="UESTC" width="20.842" height="20"> [University of Electronic Science and Technology of China (UESTC)](https://en.uestc.edu.cn/). 

My primary research interests include computer vision and deep learning, mainly focusing on AIGC and Multimodal. <span style="color:red"> I'm looking for self-motivated interns and full-time researchers.</span>

# 📜 Research Area
1. AIGC (e.g., GAN, Diffusion, LoRA training, FLUX, SDXL Lighting, SDXL Turbo, Hyper SD, SDXL, SD1.5, LCM, Midjourney)
2. Talking Face Generation
3. Multimodal, Direct Preference Optimization (DPO)
4. Image/Video Enhancement, Restoration and Decomposition (e.g., Intrinsic Image Decomposition)
5. Deep Learning and its Applications (e.g., Medical Images) 

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
<!-- Paper 15 MFDPO -->
<tr onmouseout="24_dpo_stop()" onmouseover="24_dpo_start()" >
<td width="20%">
<div class="one">
<div class="two" id = '24_dpo_image'><img src='./files/MFDPO_after.png'></div>
<img src='./files/MFDPO24_bibtex.png'>
</div>
<script type="text/javascript">
function 24_dpo_start() {
document.getElementById('24_dpo_image').style.opacity = "1";
}
function 24_dpo_stop() {
document.getElementById('24_dpo_image').style.opacity = "0";
}
24_dpo_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2410.15334">
    <papertitle_just>Modality-Fair Preference Optimization for Trustworthy MLLM Alignment</papertitle_just>
  </a>
  <br>
  Songtao Jiang, Yan Zhang, Ruizhe Chen, <strong>Yeying Jin</strong>, Zuozhu Liu
  <br>
  <em>arXiv</em>, 2024 <br>
  <a href="https://arxiv.org/abs/2410.15334">arXiv</a>
  |
  <a href="./files/MFDPO24_bibtex.txt">bibtex</a>
  <p></p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper 14 CGSAM -->
<tr onmouseout="24_CGSAM_stop()" onmouseover="24_CGSAM_start()" >
<td width="20%">
<div class="one">
<div class="two" id = '24_CGSAM_image'><img src='./files/CGSAM_after.png'></div>
<img src='./files/CGSAM_before.png'>
</div>
<script type="text/javascript">
function 24_CGSAM_start() {
document.getElementById('24_CGSAM_image').style.opacity = "1";
}
function 24_CGSAM_stop() {
document.getElementById('24_CGSAM_image').style.opacity = "0";
}
24_CGSAM_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2404.04514">
    <papertitle_just>Joint Visual and Text Prompting for Improved Object-Centric Perception with Multimodal Large Language Models</papertitle_just>
  </a>
  <br>
  Songtao Jiang, Yan Zhang, Chenyi Zhou, <strong>Yeying Jin</strong>, Yang Feng, Jian Wu, Zuozhu Liu
  <br>
  <em>arXiv</em>, 2024 <br>
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
<!-- Paper 13 Med-MoE -->
<tr onmouseout="emnlp24_moe_stop()" onmouseover="emnlp24_moe_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'emnlp24_moe_image'><img src='./files/emnlp24_moe_after.png'></div>
<img src='./files/emnlp24_moe_before.png'>
</div>
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
  Songtao Jiang, Tuo Zheng, Yan Zhang, <strong>Yeying Jin</strong>, Zuozhu Liu
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
<!-- Paper 12 RaindropClarity -->
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
  <p></p>
</td>
</tr>
<!-- Paper 12 RaindropClarity -->
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
  Tingting Chen*, Beibei Lin*, <strong>Yeying Jin*</strong>, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan (Equal-first author)
  <br>
<em>European Conference on Computer Vision (ECCV)</em>, 2024, Milan, Italy <br>
<a href="https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08521.pdf">arXiv</a>
|
<a href="./files/eccv24_dualrain_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- Paper 11 Dualrain -->
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
<!-- Paper 10 Super-resolution -->
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
  Beibei Lin*, <strong>Yeying Jin*</strong>, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan (Equal-first author)
  <br>
<em>In review</em>, 2024 <br>
<a href="https://arxiv.org/abs/2403.07408">arXiv</a>
|
<a href="./files/submit24_nighthaze_bibtex.txt">bibtex</a>
<p></p>
</td>
</tr>
<!-- Paper 9 NightHaze -->
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
<!-- Paper 8 Super-resolution -->
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
  <strong>Yeying Jin</strong>, Yuan Yuan, Wenhan Yang, Wei Ye, Robby T. Tan
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
<!-- Paper 7 DeS3 -->
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
  Beibei Lin*, <strong>Yeying Jin*</strong>, Wending Yan, Wei Ye, Yuan Yuan, Sunli Zhang, Robby T. Tan
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
<!-- Paper 6 NightRain -->
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
<p></p>
<p>Night image enhancement by enhancing low-light regions and suppressing light-effects regions.</p>
</td>
</tr>
<!-- Paper 5 NightEnhance, ECCV'22 -->
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
<!-- Paper 4 DC-ShadowNet, ICCV'21 -->
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
<!-- Paper 3 NightFog -->
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
<!-- Paper 2 Reflectance, AAAI'23 -->
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
<!-- Paper 1 defog, ACCV'22 -->
<!-- ###################################################################################################-->
    

<!-- ############################ Put your publications above this! ####################################-->
</tbody></table>

# 🏫 Educations
- 01.2020-01.2024: Ph.D. (Computer Vision and Deep Learning), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore (CAP: 4.75/5.00)
- 08.2017-08.2018: M.S. (Electrical and Computer Engineering), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore
- 09.2013-07.2017: B.Eng (Electrical and Computer Engineering), <img src="/files/UESTC.png" alt="UESTC" width="20.842" height="20"> UESTC, China (GPA: 3.93/4.00)

# 👔 Internship and Work Experience

- 11.2023: Senior Researcher at <img src="/files/tencent.png" alt="Tencent" width="85" height="20"> Singapore, working on AIGC.

- 06.2023-09.2023: <img src="/files/adobe.png" alt="Adobe" width="20" height="20"> [Adobe Research Intern](https://www.adobe.com/), Creative Intelligence Lab, mentored by [Connelly Barnes](http://www.connellybarnes.com/work/), worked with [Yuqian Zhou](https://yzhouas.github.io/), [Lingzhi Zhang](https://owenzlz.github.io/), [Sohrab Amirghodsi](https://www.linkedin.com/in/sohrab-amirghodsi-a89548a3/), [Eric Kee](https://www.erickee.com/).

- 01.2019-01.2020: Machine Learning Researcher at <img src="/files/biomind.png" alt="Biomind" width="80" height="20"> Singapore, advised by [Prof. Jiashi Feng](https://sites.google.com/site/jshfeng/), worked on Biomedical Image Synthesis, Super-resolution, Tumor Segmentation and Classification, expo demo for ["Deep Learning-Based End-to-end Automatic Contouring and Automated Radiation Therapy Treatment Planning System"](https://media.neurips.cc/Conferences/NeurIPS2019/NeurIPS_Expo_Book_2019.pdf).

# 🎖 Honors and Awards
- <img src="/files/aisg.png" alt="AISG" width="20" height="20"> [AI Singapore (AISG) Ph.D. Fellowship](https://aisingapore.org/research/phd-fellowship-programme/), Theme: Continuous Learning AI, Self-supervised Learning 

# 💻 Academic Services
- Reviewer: ICLR'25, NeurIPS'23-24, ECCV'22-24, CVPR'22-25, ICCV'23, TPAMI'23, IJCV'24, AAAI'23-25, TIP'23, CVIU'23, TCSVT'23, TVCJ'23, NEUCOM'23, ACCV'22-24, IJCAI'22, IJCNN'21, etc.
- Teaching Assistant: [EE5731 Visual Computing](https://tanrobby.github.io/teaching/ece_visual/index.html), EE5904 Neural Network (NUS ECE)

# 💬 Invited Talks
<table>
  <tr>
    <th>Topic</th>
    <th>Host</th>
    <th>Date</th>
  <tr>
    <td><a href="https://www.bilibili.com/video/BV1p5bFevEgP/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Raindrop Clarity: Dual-Focused, Day & Night</a></td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>09.2024</td>
  </tr>
  </tr>
  <tr>
    <td><a href="https://www.bilibili.com/video/BV1wc411v7zf/?spm_id_from=333.999.0.0&vd_source=8ae1cd92e40b380c0296eb6843da79a4">Shadow Removal using Diffusion Model</a></td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>01.2024</td>
  </tr>
  <tr>
    <td>Visibility Enhancement using Generative Model</td>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei Shanghai HiSilicon</td>
    <td>07.2023</td>
  </tr>
  <tr>
    <td>NextCam Reading Group: Light-effects Suppression</td>
    <td><img src="/files/adobe.png" alt="Adobe" width="20" height="20"> Adobe, USA</td>
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
    <td>Poster Present at VALSE</td>
    <td><img src="/files/VALSE.png" alt="VALSE" width="23.2" height="20"> Chongqing, China</td>
    <td>05.2024</td>
  </tr>
  <tr>
    <td>Poster Present at Singapore Vision Day</td>
    <td><img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore</td>
    <td>05.2023</td>
  </tr>
  <tr>
    <td>Poster Present at AI Research Symposium</td>
    <td><img src="/files/aisg.png" alt="AISG" width="20" height="20"> AISG, Singapore</td>
    <td>01.2023</td>
  </tr>
</table>






