## Entrega 5: Detalhamento das lajes e consolidação

Referências: [Aula 10](../aulas/010-detalhamento-lajes.md) e
[Aula 09](../aulas/009-detalhamento-secoes.md).

### Transferir o dimensionamento para as plantas

Prepare as quatro pranchas pedidas no enunciado: fôrma, armaduras positivas,
armaduras negativas e quadro de ferros/resumo de materiais. As áreas de aço
e os comprimentos devem corresponder à versão final da Entrega 4.

Na planta de fôrma, mantenha L1 a L4, V1 a V6 e as cotas em **centímetros**,
indicando a unidade no desenho. Registre as seções finais das vigas, com
largura de 15 cm, os pilares, as espessuras finais das lajes e as notas de
materiais e cobrimento.

Na planta positiva, indique as barras inferiores de cada direção e sua ordem
de montagem. Na planta negativa, indique as barras superiores sobre V2 e V5,
os comprimentos para os dois lados dos apoios e as armaduras de borda e canto
aplicáveis ao modelo. Faça cortes nos encontros em que a planta não esclarece
a posição das camadas.

### Ancoragem e comprimentos

Calcule a resistência de aderência e o comprimento básico pela sequência
da Aula 09:

$$
f_{bd}=\eta_1\eta_2\eta_3f_{ctd},
\qquad l_b=\frac{\phi}{4}\frac{f_{yd}}{f_{bd}}.
$$

Determine os coeficientes de acordo com o tipo de barra, a posição de
concretagem e a bitola. Obtenha o comprimento necessário com os fatores,
a relação entre área necessária e fornecida e os mínimos aplicáveis da aula.
Não suponha que metade da largura de uma viga de 15 cm já forneça a
ancoragem necessária.

Defina a extensão das barras pelas regiões de momento e pelas regras de
detalhamento da Aula 10. As barras positivas precisam de ancoragem nos
apoios; as negativas sobre V2 e V5 precisam cobrir os trechos necessários
em ambas as lajes. Ganchos, emendas, decalagem e interferências devem ser
representados quando aplicáveis, com comprimentos identificáveis no desenho.

### Quantidade e quadro de aço

Uma posição pode ser descrita, por exemplo, como **N1 Ø8 c/15 C=...**, mas o
comprimento só deve ser preenchido depois de definir a geometria e as
ancoragens da barra. Para uma faixa de distribuição entre a primeira e a
última barra separadas por $L_{dist}$:

$$
n=\left\lceil\frac{L_{dist}}{s}\right\rceil+1.
$$

Essa convenção inclui uma barra em cada extremidade da faixa definida.
Se o desenho usar afastamentos ou outra convenção, conte as barras a partir
das posições desenhadas, sem acrescentar uma barra duas vezes.

Com comprimento unitário $C$ em metros e bitola $\phi$ em milímetros:

$$
L_{total}=nC,\qquad
m_{lin}=7850\frac{\pi}{4}\left(\frac{\phi}{1000}\right)^2
\approx0{,}006165\phi^2\quad(\mathrm{kg/m}),
$$

$$
m_{total}=L_{total}m_{lin}.
$$

**Exemplo de quantitativo:** 20 barras de 8 mm com comprimento de 5,00 m
totalizam 100 m de aço. Com $m_{lin}\approx0{,}3946\text{ kg/m}$, a massa é
aproximadamente 39,46 kg. O exemplo ilustra o quadro; não é uma posição já
dimensionada para esta planta.

O quadro final informa posição, elemento, bitola, quantidade, comprimento
unitário, comprimento total e massa. Separe os quantitativos de pavimento-tipo
e cobertura se as armaduras diferirem e indique o número real de repetições.

### Resumo de concreto, fôrma e aço

Para a parcela de lajes:

$$
V_{lajes}=\sum_iA_i h_i.
$$

Defina se as áreas incluem ou excluem as faixas das vigas e mantenha essa
mesma convenção ao somar seus volumes. Desconte aberturas e evite duplicar
concreto nos encontros entre lajes, vigas e pilares. A área de fôrma deve
corresponder às superfícies efetivamente moldadas, conforme o escopo do
levantamento. A taxa de aço é

$$
\text{taxa de aço}=\frac{m_{aço}}{V_{concreto}}\quad(\mathrm{kg/m^3}),
$$

com aço e concreto referentes aos mesmos elementos.

### Consolidar a memória e conferir os arquivos

O relatório final reúne os dados de projeto, as hipóteses, os resultados
corrigidos das cinco entregas e as referências das aulas. Relacione cada
armadura da tabela de dimensionamento com sua posição na prancha. Os valores
de carga, espessura, seção e armadura devem coincidir em todos os documentos.

Confira se os PDFs correspondem aos DWGs, se as escalas e os carimbos estão
legíveis e se todos os integrantes estão identificados com nome e matrícula.
O fechamento do trabalho exige os resultados numéricos e as pranchas;
as equações e os exemplos desta solução comentada orientam sua conferência.

### Erros frequentes nesta entrega

- Detalhar barras com áreas diferentes das verificadas na memória final.
- Omitir a ordem das camadas e os comprimentos de ancoragem.
- Repetir posições diferentes com a mesma numeração no quadro de ferros.
- Usar centímetros como se fossem metros no levantamento da massa.
- Somar volumes ou massas de pavimentos com soluções diferentes sem separá-los.
