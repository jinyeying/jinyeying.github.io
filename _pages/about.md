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

My name is Yeying Jin. <span style="color:red"> I am actively seeking Research or Computer Vision Scientist/Engineer roles.</span>

Currently, I am a fourth-year Ph.D. student at the <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> [Department of Electrical and Computer Engineering](https://cde.nus.edu.sg/ece/) (ECE), National University of Singapore (NUS), supervised by [Prof. Robby T. Tan](http://tanrobby.github.io/). 
I had my research internship in <img src="/files/adobe.png" alt="Adobe" width="20" height="20"> Adobe, mentored by [Connelly Barnes](http://www.connellybarnes.com/work/). 
I also have 1-year working experience as a Machine Learning Research Engineer.

Previously, I completed my M.S. degree from <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> ECE, NUS; received my B.Eng degree from <img src="/files/UESTC.png" alt="UESTC" width="20.842" height="20"> [University of Electronic Science and Technology of China (UESTC)](https://en.uestc.edu.cn/). 

My primary research interests include computer vision and deep learning, mainly focusing on image translation/generation, image/video enhancement.

# 📜 Research Area
1. Generative Model (e.g., GAN, Diffusion), Image/Video Translation/Enhancement/Editing
2. Image/Video Decomposition (e.g., Intrinsic Image Decomposition)
3. Low-Level Vision in Adverse Lighting and Weather Conditions (e.g., Shadow/Night, Rain/Raindrop/Fog/Night Rain/Night Fog)
4. Deep Learning and its Applications (e.g., Medical Images) 

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
  
<!-- ###################################################################################################-->
<!-- Paper V ShadowDiffusion-->
<tr onmouseout="submit23_shadowdiffusion_stop()" onmouseover="submit23_shadowdiffusion_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'submit23_shadowdiffusion_image'><img src='./files/submit23_after.png'></div>
<img src='./files/submit23_before.png'>
</div>
<script type="text/javascript">
function submit23_shadowdiffusion_start() {
document.getElementById('submit23_shadowdiffusion_image').style.opacity = "1";
}
function submit23_shadowdiffusion_stop() {
document.getElementById('submit23_shadowdiffusion_image').style.opacity = "0";
}
submit23_shadowdiffusion_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2211.08089">
    <papertitle_just>ShadowDiffusion: Diffusion-based Shadow Removal using Classifier-driven Attention and Structure Preservation</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Wenhan Yang, Wei Ye, Yuan Yuan, Robby T. Tan
  <br>
<em>arXiv preprint</em>, 2023 <br>
<a href="https://arxiv.org/abs/2211.08089">arXiv</a>
|
<a href="">code</a>
|
<a href="./files/submit23_shadowdiffusion_bibtex.txt">bibtex</a>
<p></p>
<p>First diffusion-based shadow removal performs robustly on hard, soft and self shadows.</p>
</td>
</tr>
<!-- Paper V ShadowDiffusion -->
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<!-- Paper II NightEnhance, ECCV'22 -->
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
<a href="https://www.dropbox.com/s/t53xlojok9h3p3p/0982_poster.pdf?dl=0">poster</a>
|
<a href="https://www.dropbox.com/s/z2u4zx6u1aojiuz/0982_slides.pdf?dl=0">slides</a>
|
<a href="https://www.dropbox.com/sh/ro8fs629ldebzc2/AAD1BnNSR51_tCq7DVaLSC3Fa/light-effects?dl=0&subfolder_nav_tracking=1">data</a>
|
<a href="https://mp.weixin.qq.com/s/5wjV6R95SrQHXxqMnENAAw">link</a> 
<p></p>
<p>Night image enhancement by enhancing low-light regions and suppressing light-effects regions.</p>
</td>
</tr>
<!-- Paper II NightEnhance, ECCV'22 -->
<!-- ###################################################################################################-->


<!-- ###################################################################################################-->
<!-- Paper I DC-ShadowNet, ICCV'21 -->
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
<a href="https://www.dropbox.com/s/f0roq0kkoq9ha1x/DC-ShadowNet_poster.pdf?dl=0">poster</a>
|
<a href="https://www.dropbox.com/s/ymgf7mld0j5zrjw/DC-ShadowNet_slides.pdf?dl=0">slides</a>
<p></p>
<p>First unsupervised hard and soft shadow removal.</p>
</td>
</tr>
<!-- Paper I DC-ShadowNet, ICCV'21 -->
<!-- ###################################################################################################-->


<!-- Paper VI NightFog-->
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
  <strong>Yeying Jin</strong>, Beibei Lin*, Wending Yan, Wei Ye, Yuan Yuan, Robby T. Tan (Equal-first author)
  <br>
<em>ACM Multimedia (ACM'MM)</em>, 2023, Ottawa, Canada <br>
<a href="https://arxiv.org/abs/2308.01738">arXiv</a>
|
<a href="https://github.com/jinyeying/nighttime_dehaze"><img src="https://img.shields.io/github/stars/jinyeying/nighttime_dehaze?style=social&label=Stars"></a>
|
<a href="./files/acmmm23_nightdehaze_bibtex.txt">bibtex</a>
<p></p>
<p>First learning-based network handling nighttime haze and glow using APSF.</p>
</td>
</tr>
<!-- Paper VI NightFog -->
<!-- ###################################################################################################-->
  
<!-- ###################################################################################################-->
<!-- Paper IV Reflectance, AAAI'23 -->
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
<!-- Paper IV Reflectance, AAAI'23 -->
<!-- ###################################################################################################-->
  
  
<!-- ###################################################################################################-->
<!-- Paper III defog, ACCV'22 -->
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
<!-- Paper III defog, ACCV'22 -->
<!-- ###################################################################################################-->
    

<!-- ############################ Put your publications above this! ####################################-->
</tbody></table>

# 🏫 Educations
- Jan'2020-Jan'2024: Ph.D. (Computer Vision and Deep Learning), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore (CAP: 4.75/5.00)
- Aug'2017-Aug'2018: M.S. (Electrical and Computer Engineering), <img src="/files/NUS.png" alt="NUS" width="42.5" height="20"> NUS, Singapore
- Sep'2013-Jul'2017: B.Eng (Electrical and Computer Engineering), <img src="/files/UESTC.png" alt="UESTC" width="20.842" height="20"> UESTC, China (GPA: 3.93/4.00)

# 👔 Internships and Work Experience
- Jan'2019-Jan'2020: Machine Learning Research Engineer at <img src="/files/biomind.png" alt="Biomind" width="80" height="20"> Singapore, advised by [Prof. Feng Jiashi](https://sites.google.com/site/jshfeng/), worked intensively on Biomedical Image Translation, Synthesis, Super-resolution, Tumor Segmentation and Classification, expo demo for ["Deep Learning-Based End-to-end Automatic Contouring and Automated Radiation Therapy Treatment Planning System"](https://media.neurips.cc/Conferences/NeurIPS2019/NeurIPS_Expo_Book_2019.pdf) in [Neural Information Processing Systems (NeurIPS)'2019](https://nips.cc/Conferences/2019).

# 🎖 Honors and Awards
- <img src="/files/aisg.png" alt="AISG" width="20" height="20"> [AI Singapore (AISG) Ph.D. Fellowship](https://aisingapore.org/research/phd-fellowship-programme/), Theme: Continuous Learning AI, Self-supervised Learning 

# 💻 Academic Services
- Reviewer: CVPR'24, TPAMI'23, AAAI'24, NeurIPS'23, ICCV'23, TIP'23, CVPR'23, AAAI'23, CVIU'23, TCSVT'23, TVCJ'23, NEUCOM'23, ACCV'22, ECCV'22, CVPR'22, IJCAI'22, IJCNN'21, etc.
- Teaching Assistant: [EE5731 Visual Computing](https://tanrobby.github.io/teaching/ece_visual/index.html), EE5904 Neural Network (NUS ECE)

# 💬 Invited Talks
<table>
  <tr>
    <th>Topic</th>
    <th>Host</th>
    <th>Date</th>
  </tr>
  <tr>
    <td>Visibility Enhancement using Generative Model</td>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei Shanghai HiSilicon</td>
    <td>Jul 2023</td>
  </tr>
  <tr>
    <td>NextCam Reading Group: Light-effects Suppression</td>
    <td><img src="/files/adobe.png" alt="Adobe" width="20" height="20"> Adobe, USA</td>
    <td>Jul 2023</td>
  </tr>
  <tr>
    <td>Image/Video Restoration</td>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei Shanghai HiSilicon</td>
    <td>Mar 2023</td>
  </tr>
  <tr>
    <td>Intrinsic Image Decomposition</td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>Feb 2023</td>
  </tr>
  <tr>
    <td>Diffusion Model in Image Processing</td>
    <td><img src="/files/ByteDance.png" alt="ByteDance" width="110.77" height="20">, (invited by <a href="https://hanshuyan.github.io/">Hanshu Yan</a>)</td>
    <td>Jan 2023</td>
  </tr>
  <tr>
    <td>Visibility Enhancement in Nighttime</td>
    <td><img src="/files/huawei.png" alt="Huawei" width="19.978" height="20"> Huawei, Singapore</td>
    <td>Dec 2022</td>
  </tr>
  <tr>
    <td>Unsupervised Image Restoration and Generation</td>
    <td><img src="/files/AITIME.png" alt="AITIME" width="19.778" height="20"> AI TIME</td>
    <td>Nov 2022</td>
  </tr>
  <tr>
    <td>Poster Present at Singapore Vision Day</td>
    <td><img src="/files/NUS.png" alt="NUS" width="42.5" height="20">, Singapore</td>
    <td>May 2023</td>
  </tr>
  <tr>
    <td>Poster Present at AAAI'23</td>
    <td><img src="/files/AAAI.png" alt="AAAI" width="28.026" height="20">, Washington DC, USA</td>
    <td>Feb 2023</td>
  </tr>
  <tr>
    <td>Poster Present at AI Research Symposium</td>
    <td><img src="/files/aisg.png" alt="AISG" width="20" height="20"> AISG, Singapore</td>
    <td>Jan 2023</td>
  </tr>
  <tr>
    <td>Poster Present at ECCV'22</td>
    <td><img src="/files/ECCV.png" alt="ECCV" width="38.038" height="20">, Tel Aviv, Israel</td>
    <td>Oct 2022</td>
  </tr>
</table>






