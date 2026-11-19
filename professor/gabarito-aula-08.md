# Gabarito e notas do professor: Aula 07

Material de uso do professor. Este arquivo fica fora de `source/` e não integra o site.

## Recorte didático do capítulo 4

A aula desenvolve a dedução de compatibilidade e equilíbrio até as expressões de $\xi$ e $A_s$. As fronteiras dos domínios, os limites de ductilidade, o método simplificado do domínio 2 e as verificações construtivas aparecem sem novas deduções. Foram omitidos o processo iterativo de redução da tensão no domínio 2, as extensas tabelas adimensionais, os furos e as aberturas em vigas, além dos exemplos repetidos do capítulo.

As equações da conversão Markdown estavam como marcadores de imagens. As expressões gerais de $\xi$ e $A_s$ e a expressão de $\varphi_{max}$ foram conferidas nas imagens incorporadas ao DOCX original. A ilustração usada na aula é a Figura 4.9 desse arquivo.

O capítulo restringe a aplicação do critério de ductilidade em vários exemplos às seções sobre apoios. Para oferecer um roteiro inicial uniforme, a aula declara explicitamente a adoção do limite em todas as seções dos exercícios, sem redistribuição. Não se reproduzem aqui as discussões sobre redistribuição ou rotação plástica do capítulo.

No domínio 2, a aula adota o método simplificado dos autores. Com a limitação de $\varphi$, o equilíbrio de momentos determina a área. A linha neutra obtida antes dessa limitação é auxiliar e não deve ser usada para afirmar que o equilíbrio do bloco original permanece exato.

## Exercício 1

Dados: $b_w=200$ mm, $h=500$ mm, $d=450$ mm, C30, CA-50 e $M_d=120$ kN m.

| Grandeza | Resultado |
|---|---:|
| $f_{cd}$ | 21,4286 MPa |
| $f_{yd}$ | 434,7826 MPa |
| $\mu$ | 0,138272 |
| $\xi$ pelo bloco retangular | 0,223283 |
| Enquadramento pelo método simplificado | Domínio 2b |
| $\varphi$ | 0,910687 |
| $\varphi_{adot}$ | 0,910687, inferior a 0,930864 |
| $z$ | 409,809 mm |
| $A_s$ | 673,484 mm² = 6,735 cm² |
| $A_{s,min}$ | 1,50 cm² |
| $A_{s,nec}$ | 6,735 cm² |

A seção atende ao limite adotado $\xi\leq0,45$. O limitador de braço de alavanca não atua neste exemplo. Não usar $\varepsilon_c=3,5$‰ para inferir a deformação final do aço no domínio 2: neste domínio, o limite convencional é $\varepsilon_s=10$‰ e a deformação do concreto é menor que $\varepsilon_{cu}$.

## Exercício 2

Dados do Exemplo 2, com $M_d=3$ kN m na faixa de 1 m.

| Grandeza | Resultado |
|---|---:|
| $d$ | 131 mm |
| $\mu$ | 0,00815803 |
| $\xi$ pelo bloco retangular | 0,0120552 |
| $\varphi$ inicial | 0,995178 |
| $\varphi_{adot}$ | 0,930864 |
| $A_s$ calculado | 56,584 mm²/m = 0,566 cm²/m |
| $A_{s,min}$ positivo bidirecional | 160,8 mm²/m = 1,608 cm²/m |
| $A_{s,nec}$ | 1,608 cm²/m |

Por área, barras de 8 mm poderiam ter espaçamento de aproximadamente 312,6 mm. O limite de espaçamento da armadura principal, $\min(2h;200\text{ mm})$, reduz esse valor a 200 mm. Uma escolha é **$\phi8$ a cada 20 cm**, que fornece 251,33 mm²/m = 2,513 cm²/m.

Ponto para discussão: a armadura mínima governa a área necessária, mas o espaçamento máximo governa a área efetivamente fornecida com a bitola escolhida.

## Exercício 3

Dados do Exemplo 1, alterando apenas o concreto para C50.

| Grandeza | Resultado |
|---|---:|
| $f_{cd}$ | 35,7143 MPa |
| $\eta_c=(40/50)^{1/3}$ | 0,928318 |
| $\alpha_c$ e $\lambda$ | 0,85 e 0,80 |
| $\mu$ | 0,124444 |
| $\xi$ pelo bloco retangular | 0,215759 |
| Enquadramento pelo método simplificado | Domínio 2b |
| $\varphi$ | 0,913697 |
| $\varphi_{adot}$ | 0,913697 |
| $A_s$ | 1006,899 mm² = 10,069 cm² |

A seção atende a $\xi\leq0,45$, e a área de flexão governa sobre o mínimo. A área cai de 10,726 cm² para 10,069 cm², redução de aproximadamente 6,1%. Com $M_d$, $d$ e $f_{yd}$ fixos, o ganho vem do aumento do braço de alavanca, que é limitado pela própria altura útil. A área de aço não varia inversamente com $f_{ck}$.

## Perguntas de fechamento

- Por que é necessário verificar o limite de ductilidade mesmo quando a equação de segundo grau tem raiz real?
- Por que mudar a bitola ou o número de camadas pode exigir novo dimensionamento?
- No cálculo de lajes, em que momento se converte o momento por metro em momento de uma faixa?
- Por que a aprovação no ELU não substitui a verificação de flecha com a armadura escolhida?
