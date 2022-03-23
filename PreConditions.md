|Name  | PreConditions                                      | Effects  |Cost |
|------|----------------------------------------------------|----------|-----|
|up    | y<0 && livre(x, y-1) && n_passou(x+-1, y-1 || y-2) | y=y-1    | 1   |
|down  | y>-n && livre(x, y+1) && n_passou(x+-1, y+1 || y+2)| y=y+1    | 1   |
|left  | x>0  && livre(x-1, y) && n_passou(x-1 || x-2, y+-1)| x=x-1    | 1   |
|right | x<n  && livre(x+1, y) && n_passou(x+1 || x+2, y+-1)| x=x+1    | 1   |
