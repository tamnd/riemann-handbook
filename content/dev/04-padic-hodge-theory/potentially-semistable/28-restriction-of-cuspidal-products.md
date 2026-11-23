---
title: Harish-Chandra restriction of products of cuspidal characters
decls:
  - GlobalTheory.GLq.ResCuspProd.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Harish-Chandra restriction of products of cuspidal characters

This section computes the Harish-Chandra restriction of a product of cuspidal characters of finite general linear groups. Let $\chi_1, \dots, \chi_k$ be cuspidal characters of $\mathrm{GL}_{d_1}, \dots, \mathrm{GL}_{d_k}$ over a prime field, and let $\chi_1 \circ \cdots \circ \chi_k$ be their Harish-Chandra product, a class function on $\mathrm{GL}_n$ with $n = \sum_i d_i$. Its restriction to the Levi subgroup $\mathrm{GL}_a \times \mathrm{GL}_b$ is a sum over the ways to split the list into two parts of degrees $a$ and $b$: each cuspidal factor goes, whole, to one side. This is the form of the Mackey formula for cuspidal data (F. Digne and J. Michel, *Representations of finite groups of Lie type*, LMS Student Texts 21, Cambridge University Press, 1991, Chapter 5). The result is used to compute the derivatives of such products, and with them their generic constituents, in the trunk step [EveryCharacter](/step/every-character/).

The section is independent of the rest of the chapter. We use [parabolic induction](/learn/representations/#parabolic-induction-and-the-jacquet-module), [cuspidal representations](/learn/representations/#cuspidal-representations-and-segments) and [parabolic subgroups](/learn/groups/#parabolic-subgroups) from Volume 1.

### Induction and restriction

Let $q$ be a prime and $G_n = \mathrm{GL}_n(\mathbb{Z}/q)$. A *class function* on a group is a function to $\mathbb{C}$ that is constant on conjugacy classes. For a matrix $M$ of size $n$ and $a, b \geq 0$, let $M^{\mathrm{tl}}$ be the top left block of size $a$ and $M^{\mathrm{br}}$ the block of size $b$ that starts at row and column $a$.

**Definition 6.28.1 (Parabolic subgroup, induction, restriction).** Let $a, b \geq 0$ and $n \geq 0$.

1. A matrix $M$ of size $n$ is *in $P_a$* if $M_{ij} = 0$ whenever $j < a \leq i$.
2. For $\Phi : G_a \times G_b \to \mathbb{C}$, the *Harish-Chandra induction* of $\Phi$ is the function on $G_n$
$$R_{a,b}(\Phi)(x) = \frac{1}{\# (P_a \cap G_n)} \sum_{\substack{y \in G_n \\ y^{-1} x y \in P_a}} \Phi\big((y^{-1}xy)^{\mathrm{tl}}, (y^{-1}xy)^{\mathrm{br}}\big).$$
For $\alpha$ on $G_a$ and $\beta$ on $G_b$ write $\alpha \circ \beta = R_{a,b}(\alpha \otimes \beta)$, where $(\alpha \otimes \beta)(u, v) = \alpha(u)\beta(v)$.
3. For $\chi : G_n \to \mathbb{C}$, the *Harish-Chandra restriction* of $\chi$ is the function on $G_a \times G_b$
$$R^*_{a,b}(\chi)(h_1, h_2) = q^{-ab} \sum_{\substack{x \in G_n \cap P_a \\ x^{\mathrm{tl}} = h_1,\ x^{\mathrm{br}} = h_2}} \chi(x).$$

Lean: `GlobalTheory.GLq.hcT` (also `GlobalTheory.GLq.InPar`, the parabolic, `GlobalTheory.GLq.hc`, the product, and `GlobalTheory.GLq.res`, the restriction).

When $n = a + b$, the matrices of $G_n$ in $P_a$ form the block upper triangular parabolic subgroup, with Levi quotient $G_a \times G_b$ and unipotent radical of order $q^{ab}$. Then $R_{a,b}$ is inflation to the parabolic followed by induction, written as an average over conjugates, and $R^*_{a,b}(\chi)(h_1, h_2)$ is the average of $\chi$ over the coset of the unipotent radical above $(h_1, h_2)$.

**Definition 6.28.2 (Products of lists, cuspidal characters).** A *datum* is a pair $(d, \chi)$ with $d \geq 0$ and $\chi$ a function on $G_d$. For a list $L$ of data let $d(L)$ be the sum of the degrees.

1. The *product* of $L$ in $G_n$ is defined by recursion: the product of the empty list is the constant $1$, and the product of $(d, \chi) :: L$ is $\chi \circ \Pi(L)$ in $G_n$, where $\Pi(L)$ is the product of $L$ in $G_{d(L)}$. We write $\Pi(L)$ for the product in $G_{d(L)}$.
2. A function $\chi$ on $G_d$ is *cuspidal* if $d > 0$, $\chi$ is the character of a simple finite dimensional complex representation of $G_d$, and $R^*_{a, d-a}(\chi)(1, 1) = 0$ for every $0 < a < d$.

Lean: `GlobalTheory.GLq.hcL` (also `GlobalTheory.GLq.degL`, the degree, and `GlobalTheory.GLq.IsCusp`, cuspidal characters).

So for $L = ((d_1, \chi_1), \dots, (d_k, \chi_k))$ the product is $\chi_1 \circ (\chi_2 \circ (\cdots \circ (\chi_k \circ 1)))$. For a subset $I$ of the positions $\{0, \dots, k-1\}$ write $L_I$ for the sublist of the entries at positions in $I$, in their order in $L$, and $I^c$ for the complement.

We use the following facts, proved elsewhere in this development.

1. (Mackey formula.) Let $n = a + b = c + d$ and let $\Phi$ on $G_a \times G_b$ be a class function in each variable. Then $R^*_{c,d}(R_{a,b}\Phi)(h_1, h_2)$ is the sum over the $i$ with $0 \leq i \leq a$, $i \leq c$ and $c - i \leq b$ of
$$\begin{aligned} &R_{i, c-i}\Big( (y_1, y_3) \mapsto R_{a-i,\, b-c+i}\big( (y_2, y_4) \mapsto \\ &\qquad R^*_{i, a-i}\big(x \mapsto R^*_{c-i,\, b-c+i}(\Phi(x, \cdot))(y_3, y_4)\big)(y_1, y_2) \big)(h_2) \Big)(h_1), \end{aligned}$$
where the outer induction is in $G_c$ and the inner one in $G_d$.
2. (Cuspidal restriction.) If $\chi$ on $G_d$ is cuspidal and $0 < a < d$, then $R^*_{a, d-a}(\chi)(x, y) = 0$ for all $x, y$.
3. (Class functions.) Characters of representations, and all functions $R_{a,b}(\Phi)$, are class functions.

The Mackey formula is the double coset decomposition $P_c \backslash G_n / P_a$: the double cosets are indexed by $i$, the size of the block of $G_a$ that lands in $G_c$. Fact 2 extends the vanishing at $(1, 1)$ in the definition to all of $G_a \times G_{d-a}$.

We also use the following elementary rules, which follow from the definitions. Restriction is linear in $\chi$. For $\chi$ on $G_n$, $R^*_{0,n}(\chi)(y_1, y_2) = \chi(y_2)$ and $R^*_{n,0}(\chi)(y_1, y_2) = \chi(y_1)$. For a class function $\psi$ on $G_a$, the induction $R_{0,a}$ of $(u, v) \mapsto \psi(v)$ is $\psi$. Induction is linear in $\Phi$.

### The restriction formula

**Theorem 6.28.3 (Restriction of a cuspidal product).** Let $q$ be a prime, $L = ((d_0, \chi_0), \dots, (d_{k-1}, \chi_{k-1}))$ a list of data with every $\chi_j$ cuspidal, and $a, b \geq 0$ with $d(L) = a + b$. Then for all $x \in G_a$ and $y \in G_b$,
$$R^*_{a,b}\big(\Pi(L)\big)(x, y) = \sum_{\substack{I \subseteq \{0, \dots, k-1\} \\ \sum_{j \in I} d_j = a}} \Pi(L_I)(x) \cdot \Pi(L_{I^c})(y).$$

Lean: `GlobalTheory.GLq.ResCuspProd.main`.

The products on the right are in $G_a$ and $G_b$: $d(L_I) = a$ by the condition on $I$, and $d(L_{I^c}) = d(L) - a = b$.

*Proof.* Induction on $L$.

The empty list. Then $a = b = 0$, the product is $1$, and $R^*_{0,0}(1) = 1$. The only subset is $I = \emptyset$, and its term is $1 \cdot 1$.

The step. Let the list be $(e, \rho) :: L$, with $\rho$ cuspidal and every entry of $L$ cuspidal. Then $e > 0$, $\rho$ is a class function by fact 3, and $e + d(L) = a + b$. Write $\psi = \Pi(L)$, a class function on $G_{d(L)}$, so the product is $R_{e, d(L)}(\rho \otimes \psi)$. The Mackey formula, with $(a, b, c, d)$ replaced by $(e, d(L), a, b)$ and $\Phi = \rho \otimes \psi$, writes $R^*_{a,b}$ of the product as a sum over the $i$ with $0 \leq i \leq e$, $i \leq a$ and $a - i \leq d(L)$. By linearity of restriction, the innermost function factors as
$$R^*_{i, e-i}(\rho)(y_1, y_2) \cdot R^*_{a-i,\, d(L)-a+i}(\psi)(y_3, y_4).$$

The middle terms. If $0 < i < e$, then $R^*_{i, e-i}(\rho) = 0$ by fact 2, so the term vanishes. Since $e > 0$, there remain the terms $i = 0$ and $i = e$.

The term $i = 0$. It exists only if $a \leq d(L)$. Then $R^*_{0,e}(\rho)(y_1, y_2) = \rho(y_2)$. By induction, applied to $L$ and the pair $(a, d(L) - a)$,
$$R^*_{a,\, d(L)-a}(\psi)(y_3, y_4) = \sum_{J,\ d(L_J) = a} \Pi(L_J)(y_3)\, \Pi(L_{J^c})(y_4),$$
with $J$ a set of positions of $L$. The outer induction is $R_{0,a}$ of a function that depends only on $y_3$ and is a class function in it, so it is evaluation at $x$. By linearity, the inner induction gives $R_{e, b-e}(\rho \otimes \Pi(L_{J^c}))(y) = \Pi((e, \rho) :: L_{J^c})(y)$. So the term is
$$\sum_{J,\ d(L_J) = a} \Pi(L_J)(x) \cdot \Pi\big((e, \rho) :: L_{J^c}\big)(y).$$

The term $i = e$. It exists only if $e \leq a$. Then $R^*_{e, 0}(\rho)(y_1, y_2) = \rho(y_1)$, and the inner induction is $R_{0, b}$, which is evaluation at $y$ as above. The induction hypothesis for $L$ and the pair $(a - e, d(L) - a + e)$, together with linearity of the outer induction $R_{e, a-e}$, gives
$$\sum_{J,\ d(L_J) = a - e} \Pi\big((e, \rho) :: L_J\big)(x) \cdot \Pi(L_{J^c})(y).$$

Comparison. A set of positions of $(e, \rho) :: L$ is either $J$ shifted by one, which does not contain the position $0$ of $\rho$, or $\{0\}$ together with $J$ shifted by one. In the first case the sublist is $L_J$ and the complement is $(e, \rho) :: L_{J^c}$; in the second the sublist is $(e, \rho) :: L_J$ and the complement is $L_{J^c}$. So the right side of the theorem splits into two sums over $J$: the sets without $0$ with $d(L_J) = a$, and the sets with $0$ with $e + d(L_J) = a$. These are the two terms above. If $a > d(L)$, the first sum is empty, since $d(L_J) \leq d(L)$, and so is the term $i = 0$. If $e > a$, the second sum is empty, and so is the term $i = e$. $\square$

The proof shows why cuspidality is needed: a cuspidal factor contributes to the restriction only through the two blocks of size $0$ and $e$, so it cannot be cut in two. Without fact 2, the middle terms would give a sum over all ways to cut each factor.

**Remark 6.28.4 (Formalization).** The prime is called `g` in the Lean code, and the groups are $\mathrm{GL}_n$ over `ZMod g`, so only prime fields occur. Cuspidality ([LabelDatum.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean#L64)) asks for the vanishing of the restriction only at $(1, 1)$ and only for the maximal parabolics; fact 2 is `GlobalTheory.T.harishChandraRestrictionTwoBlock_cuspidal_eq_zero`. The induction `hcT` ([LabelDatum.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean#L40)) is defined for every $n$, not only $n = a + b$, and `toG` returns $1$ when a block is not invertible; for $n = a + b$ the blocks of an element of $P_a$ are invertible. Fact 1 is `GlobalTheory.T.mackey_formula_harishChandra_restriction_induction`, and fact 3 is `isClass_of_isIrr` and `isClass_hcT`. In the proof, the middle, first and last terms are `collapse_mid`, `collapse_left` and `collapse_right`, and the splitting of the subsets is `sum_subsets_fin_succ`. The statement sits in a file of the $p$-adic chapter, and it has a second name, `GlobalTheory.T.harishChandraRestriction_cuspidal_product_sum_subsets`, which the outline does not list.

## Notes and references

This chapter supplies the local part of the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/) of the proof chapter [Theta integrals and local matching](/proof/theta-matching/), and the $p$-adic monodromy theorem and the restriction formula used by the trunk step [EveryCharacter](/step/every-character/). The [[Selmer group|36YNSTESMQ]] bound of [Theorem 6.2.2](/entry/selmer-bound-at-point-main/) bounds a congruence length by a Bloch-Kato Selmer group, [[Tate-Shafarevich group|BK9WBMF56G]] terms, the class number and local terms. Sections 03 to 06 bound the local terms at the places above $\ell$ through Wach modules, and section 07 assembles the twisted torsion class theorem from three published local inputs. Global [[Artin reciprocity|7938EKMMVR]] and [[class field theory|AA943HVK6Z]] enter through section 01. Sections 08 to 12 treat dual exponentials, crystalline cocycles, torsion and Selmer lengths, sections 13 and 14 the integrality of Bhatt and Scholze, and sections 15 to 27 the $p$-adic monodromy theorem.

Sources.

- Local Tate duality and the Euler characteristic formula: J.-P. Serre, *Galois Cohomology*, Springer, Chapter II, §5.2, Theorem 2, and §5.7, Theorem 5. See also J. Milne, *Arithmetic Duality Theorems*, Chapter I, and J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, Chapter VII. These are also the inputs of section 23.
- Global class field theory and Artin reciprocity: J. Neukirch, *Algebraic Number Theory*, Springer, Chapter VI; J. Tate, Global class field theory, in J. W. S. Cassels and A. Fröhlich (eds.), *Algebraic Number Theory*, Chapter VII. The Chebotarev density theorem of section 12 is in Neukirch, Chapter VII, §13.
- The groups $H^1_e$, $H^1_f$ and $H^1_g$, the dimension formula and the duality: S. Bloch and K. Kato, *L-functions and Tamagawa numbers of motives*, in *The Grothendieck Festschrift* I, Progr. Math. 86, Birkhäuser, 1990, §3. This is the local package of section 11 and the setting of sections 23 and 24.
- Period rings and crystalline representations: J.-M. Fontaine, *Représentations p-adiques des corps locaux I*, in *The Grothendieck Festschrift* II, Progr. Math. 87, Birkhäuser, 1990; J.-M. Fontaine, *Le corps des périodes p-adiques*, and *Représentations p-adiques semi-stables*, in *Périodes p-adiques*, Astérisque 223 (1994). The second paper contains the rings $A_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ of sections 08, 16 and 22, and the third states the monodromy conjecture proved in section 15.
- The dual exponential map of section 08: K. Kato, *Lectures on the approach to Iwasawa theory for Hasse-Weil L-functions via $B_{\mathrm{dR}}$*, Lecture Notes in Math. 1553, Springer, 1993.
- Herr's complex: L. Herr, *Sur la cohomologie galoisienne des corps p-adiques*, Bull. Soc. Math. France 126 (1998).
- Wach modules: N. Wach, *Représentations p-adiques potentiellement cristallines*, Bull. Soc. Math. France 124 (1996); L. Berger, *Limites de représentations cristallines*, Compositio Math. 140 (2004).
- Tate's computation of Galois invariants and of $H^1$ in Tate twists, and the decompletion of section 10: J. Tate, *p-divisible groups*, in *Proceedings of a Conference on Local Fields*, Springer, 1967; J. Tate, *Relations between $K_2$ and Galois cohomology*, Invent. Math. 36 (1976).
- Prismatic $F$-crystals, sections 13 and 14: B. Bhatt and P. Scholze, *Prisms and prismatic cohomology*, Ann. of Math. 196 (2022); B. Bhatt and P. Scholze, *Prismatic F-crystals and crystalline Galois representations*, Camb. J. Math. 11 (2023). Breuil-Kisin modules: M. Kisin, *Crystalline representations and F-crystals*, in *Algebraic Geometry and Number Theory*, Progr. Math. 253, Birkhäuser, 2006.
- The $p$-adic monodromy theorem of section 15: L. Berger, *Représentations p-adiques et équations différentielles*, Invent. Math. 148 (2002), with the local monodromy theorem for $p$-adic differential equations of Y. André, *Filtrations de type Hasse-Arf et monodromie p-adique*, Invent. Math. 148 (2002), Z. Mebkhout, *Analogue p-adique du théorème de Turrittin et le théorème de la monodromie p-adique*, Invent. Math. 148 (2002), and K. Kedlaya, *A p-adic local monodromy theorem*, Ann. of Math. 160 (2004). Survey: P. Colmez, *Les conjectures de monodromie p-adiques*, Séminaire Bourbaki, exposé 897, Astérisque 290 (2003). Hyodo's theorem $H^1_g = H^1_{\mathrm{st}}$ of section 24 is also deduced in Berger's paper.
- Eigenvectors of Frobenius in $B_{\mathrm{cris}}^+$ and their spaces, sections 16 to 20: P. Colmez, *Espaces de Banach de dimension finie*, J. Inst. Math. Jussieu 1 (2002); P. Colmez and J.-M. Fontaine, *Construction des représentations p-adiques semi-stables*, Invent. Math. 140 (2000). A proof of the monodromy theorem through such spaces: P. Colmez, *Espaces vectoriels de dimension finie et représentations de de Rham*, Astérisque 319 (2008).
- Sen's theorem of section 27: S. Sen, *Continuous cohomology and p-adic Galois representations*, Invent. Math. 62 (1980). Ramification in $\ell$-adic Lie extensions, section 26: S. Sen, *Ramification in p-adic Lie extensions*, Invent. Math. 17 (1972); J.-P. Serre, *Local Fields*, Springer, Chapter IV; J. Ax, *Zeros of polynomials over local fields: the Galois action*, J. Algebra 15 (1970).
- Harish-Chandra induction and restriction, section 28: F. Digne and J. Michel, *Representations of finite groups of Lie type*, LMS Student Texts 21, Cambridge University Press, 1991, Chapter 5; J. A. Green, *The characters of the finite general linear groups*, Trans. Amer. Math. Soc. 80 (1955).
