# MLH-GHW / GEE API: How to use [Japan Aerospace Exploration Agency's ALOS-3](https://global.jaxa.jp/projects/sat/alos3/) dataset in [GEE Python API](https://developers.google.com/earth-engine/tutorials/community/intro-to-python-api)

Project webpage: https://indigowizard.github.io/GHW-GEE-API/

Consider ⭐ starring the project ʕ •ᴥ•ʔ ... ʕ　·ᴥ·ʔ

**IMPORTANT NOTE:** :warning:

The Earth Engine token **expires every 48H**, so after this, the layers won't show up and the webapp may seem like not working, it's not, it's just that I don't update the token from my personal google earth engine account unless you need a live demo, otherwise check the preview section.

## Description:

GHW Earth Engine API Tech Session: I built this quick project for the MLH Global Hack Week: April for APIs 's Earth Engine API tech session.

This is a demonstration on how to use [Japan Aerospace Exploration Agency's ALOS-3](https://global.jaxa.jp/projects/sat/alos3/) dataset (Advanced Land Observing Satellite) which is a 30m resilution global digital surface model (DSM) dataset to calculate terrain elevation of an area and render topography and relief of study area.


## Preview

|JAXA DSM 30m|Hillshade|Elevation|
|:--:|:--:|:--:|
|![image](https://user-images.githubusercontent.com/43890965/232165003-2fa31d0e-b84a-49bf-a46a-a21709946ece.png)|![image](https://user-images.githubusercontent.com/43890965/232165096-ae0d2bfd-1781-474e-ab56-dc1db541588a.png)|![image](https://user-images.githubusercontent.com/43890965/232165131-9f99b39a-66a3-476b-bd40-f584399c0861.png)|
|Slopes|Contour lines|Final Result - Layers Overlap|
|![image](https://user-images.githubusercontent.com/43890965/232165175-f1701243-4847-41ed-8d84-a1adc8df2751.png)|![image](https://user-images.githubusercontent.com/43890965/232165484-3f0a4f8e-b782-4d3b-8440-48c12e9de895.png)|![image](https://user-images.githubusercontent.com/43890965/232165538-1de0538d-8cfc-4f93-866e-cb2df5359aa2.png)|


## Ressources

- [JAXA: Utilizing Space Through Satellites](https://global.jaxa.jp/projects/sat/)
- [Earth Engine Data Catalog: ALOS DSM: Global 30m v3.2](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2)
- [Earth Engine Python API](https://developers.google.com/earth-engine/tutorials/community/intro-to-python-api)

