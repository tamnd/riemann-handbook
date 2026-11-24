---
title: Column layer conditions
decls:
  - GlobalTheory.LevelHecke.commensurable_of_tied
  - GlobalTheory.LevelHecke.commensurable_at_level
  - GlobalTheory.T.heckeUOperator_rational_invertible_ramifiedForms
  - GlobalTheory.Mem.Top.ColOwe.colLay_of_herm
  - GlobalTheory.Mem.Top.ColOwe.colLay_of_tied
  - GlobalTheory.Mem.Top.ColOwe.colLay_of_tie
  - GlobalTheory.Mem.Top.ColOwe.colLay_colT
  - GlobalTheory.T.columnLayerConditions_trueColumns_laterStages
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Column layer conditions

The core of the construction needs a list of conditions on the column data of each stage. Most of them are statements about the error data of the hermitian columns: the elements $\pi_G$ and $\pi_T$ that have the auxiliary primes and the level as norms, and the places over the level. The last condition is a comparison of two lattices of ramified forms at each place over the level prime $T_u$ of a word $u$. One lattice is the integral lattice of stage zero. The other is the image of a local lattice under a power of the upward Hecke operators. We prove that the two lattices are commensurable, with an explicit bound $n$ on both sides. The main step is that each upward Hecke operator $U_v$ maps ramified forms to ramified forms, keeps rational forms rational, and is injective on ramified forms. The background is in Volume 1, at [automorphic forms on adelic groups](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups), [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups) and [lattices in quadratic and hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

### Ramified forms and the Hecke lattice

Let $D$ be a stage datum and $u$ a word. Let $T_u$ be the level prime of the member at $u$, and let $v$ run over the level places of $u$, which are the places of $F$ over $T_u$ that the member records. For each $v$ there is a residue field $k_v$, and the units of $k_v$ act on the forms of stage zero by the diamond operators $\rho_v(a)$.

**Definition 1.7.1 (Ramified forms).** The norm operator at $v$ is $N_v = \sum_{a \in k_v^\times} \rho_v(a)$. A form of stage zero is ramified if it lies in the rational forms $F_0$ and is killed by $N_v$ for each level place $v$. The ramified lattice $M_{\mathrm{ram}}$ is the set of points of the ramified space whose image in the forms of stage zero lies in the integral lattice of stage zero.

**Definition 1.7.2 (Upward Hecke operator).** For a class $c$ of stage zero and a level place $v$, the forms of stage zero at $c$ have a local line $\ell$ at $v$, and the upward pairs above $c$ are the points $x$ of $\ell$ with $f(x) = 1$. The upward Hecke operator $U_v$ sends a form $\varphi$ to the form whose value at $c$ is the sum over the upward pairs $x$ of the translate of the value of $\varphi$ at the class above $x$.

**Definition 1.7.3 (The Hecke lattice).** Let $w$ be a place of the coefficient field. Let $U_w$ be the product of the operators $U_v$ over the level places $v$ that $w$ sees at a top embedding. The Hecke lattice $N_\lambda(w)$ is the image of the ramified part of the local lattice $S_0(w)$ under the operator

$$
T_u^{e(w)} \, U_w^{m},
$$

where $m$ is the number of stages and $e(w)$ is $m$ times the sum of the top weights at the level places that $w$ sees.

For a lattice $A$ over the integers of the coefficient field, we say that $x$ is in $A$ locally at $w$ if $s x \in A$ for some integer $s$ outside the prime of $w$.

### Commensurability

**Theorem 1.7.4 (Commensurability at the level).** Let $T$ be tied forms of stage zero for $D$ and $u$, such that the values of the additive character $\psi_0$ of $T$ lie in the coefficient field. Let $w$ be a place of the coefficient field. Then there is an integer $n \neq 0$ such that:

1. for each $x \in M_{\mathrm{ram}}$, the image of $n x$ lies in $N_\lambda(w)$;
2. for each $x$ whose image lies in $N_\lambda(w)$, $n x$ is in $M_{\mathrm{ram}}$ locally at $w$.

Lean: `GlobalTheory.LevelHecke.commensurable_of_tied`

*Proof.* Step 1 (Local pair maps). For each level place $v$, there is an equivariant local pair map $p_v$ on the adelic points of the unitary group of the Gram matrix of stage zero. It sends each point to a pair of lattices in the local space at $v$. At the representatives $y_c$ of the classes, $p_v(y_c)$ is the pair of the class $c$, and every value of $p_v$ is in good position at $v$. The Gram matrix is hermitian for the involution of the forms, so this existence theorem applies.

Step 2 (Adelic form of $U_v$). Each rational form $\varphi$ of stage zero is the restriction to the representatives of an adelic form $g$ of the level of $T$. Through $p_v$, the operator $U_v$ on $\varphi$ is the restriction of the upward adelic operator on $g$. To see this, we use the unramified uniformizer at $v$ and the natural upward tie of $T$. For each upward pair, they give a point $\eta$ near $v$ such that the class above the pair is the class of $y_c \eta$. The sum over the pairs is then the sum over an affine hyperplane in the local lattice.

Step 3 ($U_v$ keeps rational and ramified forms). The upward adelic operator maps adelic forms to adelic forms, so $U_v$ maps $F_0$ to $F_0$. For each level place $v'$ and $a \in k_{v'}^\times$, there are an integer $k$ that lifts $a$ and a diamond point $\delta$ with $\rho_{v'}(a)$ given by right translation by $\delta$. The upward adelic operator commutes with this translation. So $U_v$ commutes with each diamond operator, and thus with each $N_{v'}$. It follows that $U_v$ maps ramified forms to ramified forms. Because the values of $\psi_0$ lie in the coefficient field, $U_v$ maps rational points to rational points.

Step 4 ($U_v$ is injective on ramified forms). Let $\varphi = g$ on the representatives be ramified with $U_v \varphi = 0$. Then the upward adelic operator kills $g$ at each representative, and so it kills $g$ everywhere, because $g$ is determined by its values at the representatives. Since $N_v \varphi = 0$, the sum of the right translates of $g$ by the diamond points is also $0$. Fix a class $c$ and look at the values of $g$ near $y_c$ as a function on the local lattice at $v$. The downward tie of $T$ shows that this function sums to $0$ over the incidences, and the diamond relation shows that it sums to $0$ over the dilations. A function on the lattice with both properties is $0$. So $g(y_c) = 0$ for each $c$, and $\varphi = 0$.

Step 5 (Conclusion). Steps 3 and 4 say that each $U_v$ is stable on the ramified forms, keeps rationality, and is injective there. The commensurability theorem for such operators then gives $n$ with (1) and (2). $\square$

**Corollary 1.7.5 (Commensurability at the level prime).** Let $X$ be a set of stages, $H$ hermitian column data and $T_u$ tied forms of stage zero for each word $u$, which are joint with the level of $H$, such that the values of each $\psi_0$ lie in the coefficient field. Then for each word $u$ and each place $w$ with residue characteristic $T_u$, there is $n \neq 0$ with properties (1) and (2) of the theorem.

Lean: `GlobalTheory.LevelHecke.commensurable_at_level` (also `GlobalTheory.T.heckeUOperator_rational_invertible_ramifiedForms`, a second name)

*Proof.* Apply the theorem to $T_u$ and $w$. $\square$

### The column layer conditions

**Definition 1.7.6 (Column layer conditions).** Let $D$ be a stage datum, with level data $\Lambda$ and error data $\varepsilon$. The column layer conditions for $D$, $\Lambda$ and $\varepsilon$ are the following.

1. The element $\pi_G$ of $\varepsilon$ is at the level of $\Lambda$.
2. The elements $\pi_T$ of $\varepsilon$ are at the level of $\Lambda$.
3. The places that $\varepsilon$ sees and the embeddings $\tau$ that it attaches to them are those of the definitions.
4. The constant $D_\Gamma$ of the twisted chain is the same for each word $u$ and tuple $\mu$, and equals the constant of the base member.
5. The constant $D_\Gamma$ divides each Minkowski multiple $M$ for the bound $2 f N_m$.
6. The commensurability at the level prime holds for each word $u$ and each place $w$ with residue characteristic $T_u$.

**Theorem 1.7.7 (Column layer conditions from hermitian columns).** Let $X$ be a set of stages with a prestage. Assume that the constant $D_\Gamma$ of each twisted chain is the constant $D_\Gamma(E, R)$ of the fields and the ranks. Let $H$ be hermitian column data for $X$, and $T_u$ tied forms of stage zero that are joint with the level of $H$. Let $\varepsilon$ be the error data that $H$ gives. Then the column layer conditions hold for $X$, the level of $H$ and $\varepsilon$.

Lean: `GlobalTheory.Mem.Top.ColOwe.colLay_of_herm`

*Proof.* The hermitian column data give error data $\varepsilon$, with $\pi_G$ and $\pi_T$ taken from the compatibility of $H$ at level zero and at $T$, and with the places of $H$. The same existence statement gives conditions (1), (2) and (3).

For (4), the twisted chain at the base word and the reference tuple is the chain of the base member. So all the constants $D_\Gamma$ are equal to $D_\Gamma(E,R)$, and in particular to the constant of the base member.

For (5), the chain of each member is the twisted chain at the reference tuple, so its constant is $D_\Gamma(E,R)$. The fields satisfy the definite laws, so their degree $f$ is the degree of the ranks. Then $D_\Gamma(E,R)$ divides each Minkowski multiple for $2 f N_m$.

For (6), we must check that the values of $\psi_0$ lie in the coefficient field. Let $x$ be in the residue field at a place over the auxiliary prime $g_i$. Then $g_i x = 0$, so

$$
\psi_0(x)^{g_i} = \psi_0(g_i x) = 1.
$$

The coefficient field contains a primitive root of unity of order $g_i(g_i - 1)$. Its power with exponent $g_i - 1$ is a primitive $g_i$-th root of unity, so every $g_i$-th root of unity lies in the coefficient field. Thus the corollary applies. $\square$

**Corollary 1.7.8 (Column layer conditions from tied columns).** Let $X$ be a set of stages with a prestage, with the same constants $D_\Gamma$ as in the theorem. Then for tied symmetric column data $C$ for $X$, the column layer conditions hold for the level and the error data of the hermitian part of $C$.

Lean: `GlobalTheory.Mem.Top.ColOwe.colLay_of_tied`

*Proof.* The tied column data $C$ give hermitian column data and tied forms of stage zero, and they are joint with the level by the definition of tied column data. Apply the theorem. $\square$

**Corollary 1.7.9 (Column layer conditions for true columns).** Let $I$ be true column choices with laws $l$ and a later stage $Z$. Then for tied symmetric column data $C$ for the stage datum of $I$ at $l$ and $Z$, the column layer conditions hold for the level and the error data of the hermitian part of $C$.

Lean: `GlobalTheory.Mem.Top.ColOwe.colLay_of_tie`

*Proof.* The columns of $I$ at the laws $l$ have the constant $D_\Gamma(E,R)$ at each word and tuple, by definition. The prestage of $I$ gives a prestage of the stages. Apply the corollary above. $\square$

**Theorem 1.7.10 (Column layer conditions at later stages).** Let $w$ be a column datum over a base $B$, with frame $f$ and twist data $T$. Let $Z$ be a later stage and $t$ column data for $w$ and $Z$. Then the column layer conditions hold for the stage datum of $w$ at $Z$, the level of the full hermitian column data of $t$, and the error data of that hermitian data.

Lean: `GlobalTheory.Mem.Top.ColOwe.colLay_colT` (also `GlobalTheory.T.columnLayerConditions_trueColumns_laterStages`, a second name)

*Proof.* The column data $t$ have tied column data $C$ and full hermitian data whose hermitian part equals the hermitian part of $C$. The error data of $C$ have the same $\pi_G$, $\pi_T$ and places as the error data of the full hermitian data, so the two error data are equal. The two levels are equal for the same reason. So the claim is the last corollary for $C$. $\square$

This theorem gives the column layer conditions that the construction of the core in the next section needs at each later stage.

**Remark 1.7.11 (Formalization).** The corollary `commensurable_at_level` takes a prestage, the hermitian data $H$, the joint condition and the condition that the residue characteristic of $w$ is $T_u$, and uses none of them ([HeckeUOperatorRationalInvertibleRamifiedForms.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HeckeUOperatorRationalInvertibleRamifiedForms.lean#L251)). So the commensurability holds at every place $w$. The theorems `colLay_of_herm` and `colLay_of_tied` are in the file `MemRangeOfPowG.lean`, which is named after the lemma on roots of unity ([MemRangeOfPowG.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/MemRangeOfPowG.lean#L91)). The error data of $H$ are chosen with `Classical.choose`. The local pair maps, the commensurability theorem for stable injective operators, the adelic form values near a point, the upward operator facts, the vanishing of functions with zero sums over incidences and dilations, and the existence of the error data are cited through statement files.
