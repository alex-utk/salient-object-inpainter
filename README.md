# Salient object inpainter

## Общее описание
Проект для вставки ключевой части изображения в наиболее подохдящую фигуру из кастомного набора полигонов.

Полигоны лежат в конфиге в виде:
```
[
    [id1, x0, y0, x1, y1 ...],
    [id2, x0, y0, x1, y1 ...],
    [id3, x0, y0, x1, y1 ...]
]
```

Для работы использует [3SD](https://arxiv.org/pdf/2203.04478), OpenCV, а таже [turning function](https://ieeexplore.ieee.org/document/75509).

Для бинаризации маски используем динамический трешхолд, для кластеризации DBSCAN. Более подробно в [презентации](imgs/presentation.pdf).


![img](imgs/dynamic_tresh.png?raw=true)

---
## Демо

<video src="https://github.com/alex-utk/salient-object-inpainter/assets/46720955/25fdb5a6-ecaa-4b87-9be0-445f1e495365"></video>  

