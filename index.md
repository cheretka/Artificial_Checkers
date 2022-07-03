#  Applying Deep Reinforcement Learning Algorithms to The Game of Draughts

Student Thesis
new

Implementation of checkers (draughts) strategy board game with AI

## Usage

```python
Welcome to English draughts (checkers)!

       0     1     2     3     4     5     6     7

    +-----+-----+-----+-----+-----+-----+-----+-----+
0   |     |  r  |     |  r  |     |  r  |     |  r  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
1   |  r  |     |  r  |     |  r  |     |  r  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
2   |     |  r  |     |  r  |     |  r  |     |  r  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
3   |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
4   |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
5   |  a  |     |  a  |     |  a  |     |  a  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
6   |     |  a  |     |  a  |     |  a  |     |  a  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
7   |  a  |     |  a  |     |  a  |     |  a  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+

move: [[2, 3], [3, 4]]  ptc: 0.364
move: [[2, 3], [3, 2]]  ptc: 0.374
move: [[2, 7], [3, 6]]  ptc: 0.394
move: [[2, 1], [3, 0]]  ptc: 0.318
move: [[2, 5], [3, 4]]  ptc: 0.384
move: [[2, 1], [3, 2]]  ptc: 0.381
move: [[2, 5], [3, 6]]  ptc: 0.358
selected move: [[2, 7], [3, 6]]

       0     1     2     3     4     5     6     7

    +-----+-----+-----+-----+-----+-----+-----+-----+
0   |     |  r  |     |  r  |     |  r  |     |  r  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
1   |  r  |     |  r  |     |  r  |     |  r  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
2   |     |  r  |     |  r  |     |  r  |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
3   |     |     |     |     |     |     |  r  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
4   |     |     |     |     |     |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
5   |  a  |     |  a  |     |  a  |     |  a  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
6   |     |  a  |     |  a  |     |  a  |     |  a  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
7   |  a  |     |  a  |     |  a  |     |  a  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+

your possible moves: 
0 [[5, 0], [4, 1]]
1 [[5, 2], [4, 1]]
2 [[5, 2], [4, 3]]
3 [[5, 4], [4, 3]]
4 [[5, 4], [4, 5]]
5 [[5, 6], [4, 5]]
6 [[5, 6], [4, 7]]
please write index of your move: 6

       0     1     2     3     4     5     6     7

    +-----+-----+-----+-----+-----+-----+-----+-----+
0   |     |  r  |     |  r  |     |  r  |     |  r  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
1   |  r  |     |  r  |     |  r  |     |  r  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
2   |     |  r  |     |  r  |     |  r  |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
3   |     |     |     |     |     |     |  r  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
4   |     |     |     |     |     |     |     |  a  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
5   |  a  |     |  a  |     |  a  |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
6   |     |  a  |     |  a  |     |  a  |     |  a  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
7   |  a  |     |  a  |     |  a  |     |  a  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+

move: [[2, 3], [3, 2]]  ptc: 0.384
move: [[1, 6], [2, 7]]  ptc: 0.388
move: [[2, 1], [3, 2]]  ptc: 0.34
move: [[2, 5], [3, 4]]  ptc: 0.354
move: [[2, 3], [3, 4]]  ptc: 0.387
move: [[2, 1], [3, 0]]  ptc: 0.367
move: [[3, 6], [4, 5]]  ptc: 0.298
selected move: [[1, 6], [2, 7]]

       0     1     2     3     4     5     6     7

    +-----+-----+-----+-----+-----+-----+-----+-----+
0   |     |  r  |     |  r  |     |  r  |     |  r  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
1   |  r  |     |  r  |     |  r  |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
2   |     |  r  |     |  r  |     |  r  |     |  r  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
3   |     |     |     |     |     |     |  r  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
4   |     |     |     |     |     |     |     |  a  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
5   |  a  |     |  a  |     |  a  |     |     |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+
6   |     |  a  |     |  a  |     |  a  |     |  a  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
7   |  a  |     |  a  |     |  a  |     |  a  |     |
    +-----+-----+-----+-----+-----+-----+-----+-----+

your possible moves: 
0 [[5, 0], [4, 1]]
1 [[5, 2], [4, 1]]
2 [[5, 2], [4, 3]]
3 [[5, 4], [4, 3]]
4 [[5, 4], [4, 5]]
5 [[6, 5], [5, 6]]
6 [[6, 7], [5, 6]]
please write index of your move: 6
```


### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/cheretka/Deep_Learning_and_Draughts/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
