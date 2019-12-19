# A mathematical model of the pressure of an extreme ideology on a society

Based (very freely) on Santonja, Francisco J., Ana C. Tarazona, and Rafael J. Villanueva. "A mathematical model of the pressure of an extreme ideology on a society." Computers & Mathematics with Applications 56.3 (2008): 836-846.

## Groups of parties

- Group G1: Non-nationalist parties against independence and the use of violence;
- Group G2: Nationalist parties agreeing with independence but disagreeing with the use of violence;
- Group G3: Nationalist parties agreeing with independence and the use of violence.

## Subpopulations

- <img src="https://render.githubusercontent.com/render/math?math=E\left ( t \right )">: Number of people who share the common ideological characteristics of parties in G1 at time t;
- <img src="https://render.githubusercontent.com/render/math?math=N\left ( t \right )">: Number of people who share the common ideological characteristics of parties in G2 at time t;
- <img src="https://render.githubusercontent.com/render/math?math=V\left ( t \right )">: Number of people who share the common ideological characteristics of parties in G3 at time t;
- <img src="https://render.githubusercontent.com/render/math?math=A\left ( t \right )">: The rest of people at time t. It includes people who do not share the ideological characteristics of groups G1, G2 and G3 or people who abstain.

## Model

![](images/diagram.png)

Lets consider a population subdivised into this 4 groups (E, N, V, A). Then, lets assume that:

- The number of births <img src="https://render.githubusercontent.com/render/math?math=\Lambda\left ( t \right )"> and the number of deaths <img src="https://render.githubusercontent.com/render/math?math=\Phi\left ( t \right )"> are proportional to the number of individuals in each subpopulation;
- Terrorism does not increase substantially the number of deaths;
- The imigration <img src="https://render.githubusercontent.com/render/math?math=\Gamma\left ( t \right )"> and the emigration <img src="https://render.githubusercontent.com/render/math?math=\Sigma\left ( t \right )"> are included. It is considered that only occurs in subpopulations E and A due to the terror pressure in proportions <img src="https://render.githubusercontent.com/render/math?math=\alpha_{1}"> and <img src="https://render.githubusercontent.com/render/math?math=\alpha_{2}">, respectively.

Then, the system of equations that models the evolution of ideologies (under pressure of the violence) is given by:

- <img src="https://render.githubusercontent.com/render/math?math=\beta_{1} > 0"> indicates that the transition is due the pressure of violent acts and <img src="https://render.githubusercontent.com/render/math?math=\beta_{1} < 0"> indicates a strict law enforcement;
- <img src="https://render.githubusercontent.com/render/math?math=k > 0">;
- <img src="https://render.githubusercontent.com/render/math?math=E'\left ( t \right ) = \Lambda\left ( t \right )E\left ( t \right ) + \alpha_{2}\Gamma\left ( t \right ) - \beta_{1}E\left ( t \right )\frac{V\left ( t \right )}{T\left ( t \right )} - \Phi\left ( t \right )E\left ( t \right ) - \alpha_{1}\Sigma\left ( t \right )">;
- <img src="https://render.githubusercontent.com/render/math?math=N'\left ( t \right ) = \Lambda\left ( t \right )N\left ( t \right ) - \beta_{2}N\left ( t \right )\frac{E\left ( t \right )}{T\left ( t \right )} - \Phi\left ( t \right )N\left ( t \right )">;
- <img src="https://render.githubusercontent.com/render/math?math=V'\left ( t \right ) = \Lambda\left ( t \right )V\left ( t \right ) + k\beta_{1}A\left ( t \right )\frac{V\left ( t \right )}{T\left ( t \right )} - \Phi\left ( t \right )V\left ( t \right )">;

- <img src="https://render.githubusercontent.com/render/math?math=A'\left ( t \right ) = \Lambda\left ( t \right )A\left ( t \right ) + \left ( 1 - \alpha_{2} \right ) \Gamma \left ( t \right ) + \beta_{1}E\left ( t \right )\frac{V\left ( t \right )}{T\left ( t \right )} + \beta_{2}N\left ( t \right )\frac{E\left ( t \right )}{T\left ( t \right )} - k\beta_{1}A\left ( t \right )\frac{V\left ( t \right )}{T\left ( t \right )} - \Phi\left ( t \right )A\left ( t \right ) - \left ( 1 - \alpha_{1} \right ) \Sigma \left ( t \right )">;

- <img src="https://render.githubusercontent.com/render/math?math=T\left ( t \right ) = E\left ( t \right ) + N\left ( t \right ) + V\left ( t \right ) + A\left ( t \right )">.
