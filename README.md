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

Для бинаризации маски используем динамический трешхолд, для кластеризации DBSCAN. Более подробно в [презентации](aaa)

[Contribution guidelines for this project](docs/CONTRIBUTING.md)
---
## Демо

<video src="https://user-images.githubusercontent.com/126239/151127893-5c98ba8d-c431-4a25-bb1f-e0b33645a2b6.mp4"></video>