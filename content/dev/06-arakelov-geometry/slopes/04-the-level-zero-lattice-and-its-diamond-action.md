---
title: The level-zero lattice and its diamond action
decls:
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_diamonds
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_split
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The level-zero lattice and its diamond action

This section applies the results of Section 3 to the lattice of automorphic forms of level zero. The diamond operators at the places above a level prime $T$ give an action of a product of $f$ copies of $\mathbb{F}_T^\times$, and the forms that vanish under every norm of this action form the ramified subspace. We construct an orthogonal slice for this action, under four conditions on the data, and conclude that the slope of the ramified sublattice is the slope of the whole lattice minus $f \log(T-1)/(T-2)$. Section 5 removes the conditions one by one and arrives at [Theorem 1.5.4](/entry/slope-line-0/).

### The setting

We fix the data of the proof at one word $u$; they are described in the chapters on the global setting, and we recall only what this chapter uses.

- A Galois, totally complex number field $K$ with a fixed embedding $K \to \mathbb{C}$. All hermitian lattice data are over $K$.
- A prime number $T$, the *level prime*, a finite set $\mathfrak{v}_T$ of $f$ places, and for each $v \in \mathfrak{v}_T$ a finite field $\mathbb{F}_v$ with $T$ elements. We put $G = \prod_{v \in \mathfrak{v}_T} \mathbb{F}_v^\times$ and $e_v(a) \in G$ for $a \in \mathbb{F}_v^\times$ placed at $v$, as in Section 3.
- A finite set $\mathcal{C}$ of *level-zero classes*, each $c \in \mathcal{C}$ with a finite stabilizer group $\Gamma_c$, and a finite set $Y$. A *form* is a function $\varphi : \mathcal{C} \to \mathbb{C}^Y$, and we write $\varphi(c)$ for its value on the class $c$. The forms of level zero are a subspace $M_0$ of the space of forms.
- For each $v$ an action $a \mapsto \rho_T(v, a)$ of $\mathbb{F}_v^\times$ on the forms by linear maps that preserve $M_0$: the *diamond operators* at $v$. They are given by an action $a \mapsto a \cdot c$ of $\mathbb{F}_v^\times$ on $\mathcal{C}$, the *dilation*, and linear automorphisms $\theta(v, a, c)$ of $\mathbb{C}^Y$, through
$$
(\rho_T(v, a)\varphi)(c) = \theta(v, a, c)\big(\varphi(a \cdot c)\big).
$$
- The *norm* at $v$ is $N_v = \sum_{a \in \mathbb{F}_v^\times} \rho_T(v, a)$, and the space of *ramified forms* is $M_{\mathrm{ram}} = M_0 \cap \bigcap_v \ker N_v$.
- The *level-zero lattice* is a good hermitian lattice datum $A_0 = (V, b, X, L)$ over $K$ with an injective map $\varepsilon : V \to \{\text{forms}\}$ that is semilinear for the embedding of $K$, such that the images $\varepsilon(b_j)$ of the basis are linearly independent over $\mathbb{C}$ and span $M_0$. The diamond operators preserve $\varepsilon(L)$: for $x \in L$ there is $y \in L$ with $\varepsilon(y) = \rho_T(v, a)\varepsilon(x)$.

The *ramified subspace* is $V_{\mathrm{ram}} = \varepsilon^{-1}(M_{\mathrm{ram}})$, the *ramified lattice* is $L_{\mathrm{ram}} = L \cap V_{\mathrm{ram}}$, and $A_{\mathrm{ram}} = A_0[L_{\mathrm{ram}}]$.

**Definition 1.4.1 (Ramified slope formula).** The data satisfy the *ramified slope formula* if
$$
\mu(A_{\mathrm{ram}}) = \mu(A_0) - f\, \frac{\log(T-1)}{T-2} .
$$

By the corollary on the prime field case in Section 3, the formula holds as soon as $A_0$ is an induced datum over $G$ whose ramified subspace is $V_{\mathrm{ram}}$, and $T \geq 3$.

### The conditions

The construction uses the following conditions.

1. The *Hida setting*: $2 f N + 1 < T$, where $N \geq 1$ is the rank of the top level, together with two bounds on the weights at $T$ (an alcove condition and $4 a_{\max} < T$) and the nonnegativity of the top determinant shifts. Only one consequence is used here: since $f \geq 2$, it gives $T > 2f N + 1 \geq 5 > 3$, so $T \geq 3$.
2. *Compatible forms at level zero*. This is a datum that ties the level-zero classes, the lattice and the diamond operators to the adelic description of the forms. We use three of its consequences. First, $x \in V$ lies in $L$ if and only if, for every class $c$, the value $\varepsilon(x)(c)$ satisfies a local integrality condition $Q_c$ that depends only on $c$. Second, for every set $\mathcal{S}$ of classes and every $x \in V$, the form that agrees with $\varepsilon(x)$ on $\mathcal{S}$ and vanishes off $\mathcal{S}$ is again $\varepsilon(y)$ for some $y \in V$. Third, together with condition 4, the diamond operators at distinct places commute.
3. *Free stabilizers*: every level-zero class has trivial stabilizer, $\Gamma_c = 1$.
4. *Diamond elements*: for every $v$ and every $a \in \mathbb{F}_v^\times$ there is an integer $k$ with $k \equiv a$ in $\mathbb{F}_v$ that carries a diamond element of the level group at $v$.
5. *Orthogonal classes*: if $x, y \in V$ and for every class $c$ one of $\varepsilon(x)(c)$, $\varepsilon(y)(c)$ is zero, then $\langle x, y \rangle_v = 0$ for every infinite place $v$ of $K$.
6. *Diamond isometry*: the operators $\rho(v, a)$ on $V$ defined below preserve every majorant: $\langle \rho(v,a) x, \rho(v,a) y \rangle_w = \langle x, y \rangle_w$.

Conditions 5 and 6 say that the metric of $A_0$ is a sum over classes, and that the diamond operators move these summands isometrically. This is what one expects of a Petersson-type metric, and Section 5 proves both conditions from the compatible forms.

### The action on the lattice

Since $L$ spans $V$ and $\rho_T(v, a)$ preserves $\varepsilon(L)$, it also preserves $\varepsilon(V)$, and since $\varepsilon$ is injective there is a unique $K$-linear map $\rho(v, a) : V \to V$ with $\varepsilon \circ \rho(v,a) = \rho_T(v,a) \circ \varepsilon$. These maps form an action of $\mathbb{F}_v^\times$ on $V$ that preserves $L$. Under conditions 2 and 4 the actions at distinct places commute, so they combine into a homomorphism $\rho : G \to \operatorname{End}_K(V)$ with $\rho(e_v(a)) = \rho(v, a)$. In the same way the dilations combine into an action of $G$ on $\mathcal{C}$, and by induction on the number of places,
$$
\varepsilon(\rho(g) x)(c) = \theta_{g, c}\big( \varepsilon(x)(g \cdot c) \big) \qquad (g \in G,\ c \in \mathcal{C},\ x \in V)
$$
for a linear automorphism $\theta_{g, c}$ of $\mathbb{C}^Y$. Since the norm $N_v$ commutes with $\varepsilon$ in the same way,
$$
V_{\mathrm{ram}} = \bigcap_{v} \ker N_v^\rho, \qquad N_v^\rho = \sum_{a \in \mathbb{F}_v^\times} \rho(e_v(a)),
$$
where we used that $\varepsilon(V) \subseteq M_0$.

Under conditions 2, 3 and 4 the action of $G$ on $\mathcal{C}$ is free: if $g \cdot c = c$ then $g = 1$. This is the place where the trivial stabilizers enter. The proof identifies $G$ with $\prod_v (\mathbb{Z}/T\mathbb{Z})^\times$ through the diamond elements and uses the trivial stabilizers.

### The slice

Choose a representative $\bar c$ in each $G$-orbit of $\mathcal{C}$ and let
$$
W = \{ x \in V : \varepsilon(x)(c) = 0 \text{ for every class } c \text{ that is not a representative} \}.
$$
For each class $c$ let $h_c \in G$ be the unique element with $h_c \cdot c = \bar c$; it is unique because the action is free.

**Proposition 1.4.2 (The slice is orthogonal).** Assume conditions 2 to 6. Then the map $\Psi_W : W^G \to V$, $F \mapsto \sum_g \rho(g) F(g)$, is bijective; for $F \in W^G$, $\Psi_W(F) \in L$ if and only if $F(g) \in L$ for all $g$; and $\langle \rho(g) x, \rho(h) y \rangle_v = [g = h] \langle x, y \rangle_v$ for all $x, y \in W$. Finally, $L \neq 0$.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slice_map_bijective` (also `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slice_mem_lattice_iff`, `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slice_summands_orthogonal`, `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.lattice_level_zero_ne_bot`).

*Proof.* For $x \in W$ the form $\varepsilon(\rho(g) x)$ is supported on the classes $c$ with $g \cdot c$ a representative, that is, with $h_c = g$, and on such a class its value is $\theta_{g,c}(\varepsilon(x)(\bar c))$. So for $F \in W^G$ and a class $c$,
$$
\varepsilon(\Psi_W F)(c) = \theta_{h_c, c}\big( \varepsilon(F(h_c))(\bar c) \big).
$$
If $\Psi_W F = 0$, then the value of $\varepsilon(F(g))$ at every representative is zero, by this formula applied to $c = g^{-1} \cdot \bar c$; since $F(g) \in W$ vanishes off the representatives, $F = 0$. For surjectivity, let $x \in V$. For $g \in G$, by the second consequence of condition 2 there is $y_g \in V$ such that $\varepsilon(y_g)$ agrees with $\varepsilon(x)$ on the classes $c$ with $h_c = g$ and vanishes elsewhere. Then $\sum_g y_g = x$, and $\rho(g^{-1}) y_g$ lies in $W$, because $\varepsilon(\rho(g^{-1})y_g)$ is supported on the classes $c$ with $h_{g^{-1}\cdot c} = g$, that is, $c = \overline{c}$ a representative. So $\Psi_W\big((\rho(g^{-1})y_g)_g\big) = \sum_g y_g = x$.

For the lattice, $\rho(g)$ preserves $L$, and so does $\rho(g)^{-1} = \rho(g^{-1})$, so $F(g) \in L$ if and only if $\rho(g) F(g) \in L$. At a class $c$ only the summand $g = h_c$ contributes to $\varepsilon(\Psi_W F)(c)$, and the zero value satisfies every condition $Q_c$. So by the first consequence of condition 2, $\Psi_W(F) \in L$ if and only if each $\rho(g)F(g)$ lies in $L$.

For the orthogonality, if $g = h$ this is condition 6, extended from the generators $e_v(a)$ to all of $G$. If $g \neq h$, the forms $\varepsilon(\rho(g)x)$ and $\varepsilon(\rho(h)y)$ have disjoint supports, since a class $c$ in both supports would have $h_c = g$ and $h_c = h$. Condition 5 gives $\langle \rho(g)x, \rho(h)y \rangle_v = 0$.

Finally, the compatible forms provide a class $c_0$ and a nonzero value $w \in \mathbb{C}^Y$ such that the form supported on $c_0$ with value $w$ lies in $M_0$. Since $\varepsilon(V)$ spans $M_0$, $V \neq 0$, and since $L$ spans $V$, $L \neq 0$. $\square$

### The slope formula under the conditions

**Theorem 1.4.3 (Ramified slope formula from diamond elements).** Assume the Hida setting, compatible forms at level zero, free stabilizers, diamond elements, orthogonal classes and the diamond isometry. Then the ramified slope formula holds.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_diamonds` (also `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_compatible_slice`, `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_slice`, `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_induced`).

*Proof.* By the proposition, the slice $W$ satisfies the three conditions of the theorem on induced data from an orthogonal slice in Section 3, for the good datum $A_0$ with $L \neq 0$. That theorem gives an induced datum over $G$ with ramified subspace $\bigcap_v \ker N_v^\rho = V_{\mathrm{ram}}$. Each factor $\mathbb{F}_v^\times$ has $T - 1$ elements, there are $f$ factors, and the Hida setting gives $T \geq 3$. The corollary on the prime field case in Section 3 with $q = T$ gives the formula. $\square$

**Corollary 1.4.4 (Ramified slope formula at a split prime).** Assume the Hida setting, compatible forms at level zero, free stabilizers, orthogonal classes and the diamond isometry, and assume that the CM extension splits at every place of $\mathfrak{v}_T$: for each $v$ there is an idempotent $e$ of the local integral algebra at $v$ with $\bar e = 1 - e$ for the complex conjugation. Then the ramified slope formula holds.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_formula_of_split`

*Proof.* At a split place the local algebra is a product of two copies of the local field, exchanged by the conjugation, and the idempotent gives the diamond elements of condition 4 for every class of $\mathbb{F}_v^\times$. Then the theorem applies. $\square$

**Remark 1.4.5 (Formalization).** The datum of compatible forms at level zero is a structure with many fields, which we did not unfold; we stated only the consequences that the proofs use. Of the Hida setting only $T \geq 3$ is used ([SlopeRamifiedInducedPrimeField.lean](lean:Formalism/LocalToGlobal/GlobalTheory/GL6/DiagonalSlopes/SlopeRamifiedInducedPrimeField.lean#L288)). The passage from a split place to diamond elements, and the freeness of the action on classes, are separate results whose proofs we did not open. The same results also exist under the same names in a second copy of the file one directory higher, `GL6/SlopeRamifiedInducedPrimeField.lean`; this chapter follows the copy in `GL6/DiagonalSlopes`.
