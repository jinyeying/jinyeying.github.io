---
permalink: /
title: ""
excerpt: "Bio"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am Yeying JIN, a Ph.D. student at the [Department of Electrical and Computer Engineering](https://cde.nus.edu.sg/ece/), National University of Singapore (NUS), supervised by [Prof. Robby T. Tan](http://tanrobby.github.io/). 
Previously, I completed my M.S. degree from ECE, NUS and received my B.Eng degree from the [University of Electronic Science and Technology of China (UESTC)](https://en.uestc.edu.cn/). I also have 1.5 years of working experience as a Machine Learning Research Engineer in Singapore.
My primary research interests include computer vision and deep learning, mainly focusing on image translation/generation, image/video enhancement.

Research
======
<p style='text-align: justify;'> My previous research works were dedicated to: (1) Handling low-level vision problems and (2) Performing visibility enhancement, under degraded visibility conditions such as nighttime and daytime fog. Related publications are presented below.</p>

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
<!-- NightEnhance, ECCV'22 -->
<tr onmouseout="eccv22_nightenhance_stop()" onmouseover="eccv22_nightenhance_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'eccv22_nightenhance_image'><img src='./files/eccv22_after.png'></div>
<img src='./files/eccv22_before.png'>
</div>
<script type="text/javascript">
function eccv22_nightenhance_start() {
document.getElementById('eccv22_nightenhance_image').style.opacity = "1";
}
function eccv22_nightenhance_stop() {
document.getElementById('eccv22_nightenhance_image').style.opacity = "0";
}
cvpr21_nightenhance_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://openaccess.thecvf.com/content/CVPR2021/html/Sharma_Nighttime_Visibility_Enhancement_by_Increasing_the_Dynamic_Range_and_Suppression_CVPR_2021_paper.html">
    <papertitle_just>Unsupervised Night Image Enhancement: When Layer Decomposition Meets Light-Effects Suppression</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Robby T. Tan
  <br>
<em>European Conference on Computer Vision (ECCV)</em>, 2022, Tel Aviv, Israel <br>
<a href="https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136970396.pdf.pdf">paper</a>
|
<a href="./files/eccv22_nightenhance_bibtex.txt">bibtex</a>
|
<a href="https://www.dropbox.com/sh/ro8fs629ldebzc2/AAD1BnNSR51_tCq7DVaLSC3Fa/light-effects?dl=0&subfolder_nav_tracking=1">data</a>
<p></p>
<p></p>
</td>
</tr>
<!-- NightEnhance, ECCV'22 -->
<!-- ###################################################################################################-->
  
  
<!-- ###################################################################################################-->
<!-- DC-ShadowNet, ICCV'21 -->
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
  <a href="">
    <papertitle_just>DC-ShadowNet: Single-Image Hard and Soft Shadow Removal Using Unsupervised Domain-Classifier Guided Network</papertitle_just>     
  </a>
  <br>
  <strong>Yeying Jin</strong>, Aashish Sharma, Robby T. Tan
  <br>
<em>International Conference on Computer Vision (ICCV)</em>, 2021, Montreal, Canada <br>
<a href="">paper</a>
|
<a href="">bibtex</a>
|
<a href="https://github.com/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal">code</a>
<p></p>
<p></p>
</td>
</tr>
<!-- DC-ShadowNet, ICCV'21 -->
<!-- ###################################################################################################-->
  


<!-- ###################################################################################################-->

<!-- ############################ Put your publications above this! ####################################-->
</tbody></table>

Academic Services
======
- Reviewer: CVPR'23, AAAI'23, ACCV'22, ECCV'22, CVPR'22, IJCAI'22, IJCNN'21

- Teaching Assistant: [EE5731 Visual Computing](https://tanrobby.github.io/teaching/ece_visual/index.html), EE5904 Neural Network (NUS ECE)

Awards and Fellowships
======
- [AISG Ph.D. Fellowship](https://aisingapore.org/research/phd-fellowship-programme/), 2021

Education
======
- Jan'2020-May'2024: Ph.D. (Computer Vision and Deep Learning), NUS, Singapore (Overall CAP: 4.75/5.00)
- Aug'2017-Aug'2018: M.S. (Electrical and Computer Engineering), NUS, Singapore
- Sep'2013-Jul'2017: B.Eng (Electrical and Computer Engineering), UESTC, China (Overall GPA: 3.93/4.00)

Work Experience
======
May'2018-Jan'2020: Machine Learning Research Engineer at [BioMind](https://biomind.ai/), Singapore, advised by [Prof. Polina Golland](http://people.csail.mit.edu/polina/) and [Prof. Feng Jiashi](https://sites.google.com/site/jshfeng/)
- Biomedical Image Translation, Synthesis, Super-resolution using GAN; Tumor Segmentation and Classification
- NIPS'19 expo demo for "Deep Learning-Based End-to-end Automatic Contouring and Automated Radiation Therapy Treatment Planning System."
