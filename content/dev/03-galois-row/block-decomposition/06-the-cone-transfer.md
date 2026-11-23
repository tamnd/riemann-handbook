---
title: The cone transfer
decls:
  - GlobalTheory.T.projective_chart_affine_coords
  - GlobalTheory.CompanionTheory.ConeTransfer.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The cone transfer

The proof that the top power of a first Chern class is nonzero ends with an identity of differential forms on an affine open $V$ with coordinates. To reach that identity, a relation between cohomology classes on the thickening site must be turned into a relation between functions on $V$. This section proves the transfer. It says: if the cup product of the classes $d\log g_k$ is a sum of classes from larger opens plus a coboundary, then the logarithmic Jacobian of the $g_k$ is a sum of Jacobian forms from those opens plus a divergence. The proof lifts the data to a truncated thickening site, glues there, and reads the result on $V$ through the unique representation of top-degree classes by $f \, dt_0 \wedge \dots \wedge dt_n$.

We use the site of thickenings, the filtration $J^{[r]}$, its graded pieces $\operatorname{gr}^r = J^{[r]} / J^{[r+1]}$, and the truncated sites $\mathcal{T}_s(\mathcal{V})$ of [the previous section](/entry/affine-graded-cohomology-vanishing/). For a class $c$ in $H^m(\operatorname{gr}^r)$ we say that a cochain $z$ with values in $J^{[r]}$ and with $dz$ in $J^{[r+1]}$ *represents* $c$ if its image in $\operatorname{gr}^r$ is a cocycle of class $c$.

**Definition 8.6.1 (The setting of the transfer).** Let $K$ be a field of characteristic $0$ and $q : X \to \operatorname{Spec} K$ [[smooth|EXKGG9X6J0]] of relative dimension $n + 1$. Let $i : X \to \mathbb{P}^N_K$ be a morphism and $y_0, \dots, y_{n+1}$ homogeneous polynomials. Put $U_k = i^{-1} D_+(y_k)$, and for a nonempty $S \subseteq \{0, \dots, n+1\}$ let $U_S = \bigcap_{k \in S} U_k$. Assume each $U_S$ is affine. Write $U_{\mathrm{all}}$ for the intersection of all $U_k$ and $U_{\hat \jmath}$ for the intersection of the $U_k$ with $k \neq j$. Let $V \subseteq U_{\mathrm{all}}$ be an open with coordinates $t_0, \dots, t_n$, and $D_0, \dots, D_n$ derivations of $\mathcal{O}(V)$ over $K$ with $D_k t_l = \delta_{kl}$.

The data come from [the projection lemma](/entry/geo-setup/) of the chapter on the comparison. There the $y_k$ are the coordinates of a projection, the $U_k$ are its charts, and $V$ is a small chart with coordinates.

**Definition 8.6.2 (Jacobian forms).** Let $W \supseteq V$ be an open and $\kappa : \{1, \dots, m\} \to \{0, \dots, n\}$ injective. The module of *Jacobian forms* of $W$ of type $\kappa$ is the set of finite sums of functions
$$b \cdot \det\bigl(D_{\kappa(k)} b_l\bigr)_{k, l = 1}^{m}$$
on $V$, with $b, b_1, \dots, b_m$ restrictions to $V$ of functions on $W$.

For $\kappa$ the identity, $b \det(D_k b_l) \, dt_0 \wedge \dots \wedge dt_n = b \, db_0 \wedge \dots \wedge db_n$. So a Jacobian form of $W$ is the coefficient of an $(n+1)$-form on $V$ that extends to $W$. For $\kappa$ the map that skips $k$, it is the coefficient of $dt_0 \wedge \dots \widehat{dt_k} \dots \wedge dt_n$ in an $n$-form that extends to $W$.

**Definition 8.6.3 (Logarithmic classes).** Let $g$ be a unit on $U_{\mathrm{all}}$, and choose a lift $\hat g$ of $g$ to the structure ring of each thickening over $U_{\mathrm{all}}$, with $J^{[n+2]} = 0$. The class $d\log g$ is represented by the Čech $1$-cochain $\log(\hat g(T_1) / \hat g(T_0))$, the truncated logarithm of the ratio of the two lifts on a pair of thickenings. The ratio is $1$ modulo $J$, so the truncated series makes sense.

**Theorem 8.6.4 (Cone transfer).** In the setting above, let $g_0, \dots, g_n$ be units on $U_{\mathrm{all}}$ with lifts $\hat g_k$ as above. Let $c_0 \in H^{n+1}(\operatorname{gr}^{n+1})$ on the thickenings over $U_{\mathrm{all}}$ be the class represented by the cup product of the cochains $d\log \hat g_k$. Let $\omega_j$, for $0 \leq j \leq n + 1$, be classes in $H^{n+1}(\operatorname{gr}^{n+1})$ on the thickenings over $U_{\hat \jmath}$. Let $f$ be an $n$-cochain with values in $J^{[n]}$ such that $df$ has values in $J^{[n+1]}$ and represents $c_0 - \sum_j \omega_j|_{U_{\mathrm{all}}}$. Then there are Jacobian forms $x_j$ of $U_{\hat \jmath}$ of type the identity, and Jacobian forms $\eta_k$ of $U_{\mathrm{all}}$ of type "skip $k$", such that for one choice of sign
$$\pm \Bigl(\prod_k g_k\Bigr)^{-1} \det\bigl(D_k g_l\bigr) = \sum_{j=0}^{n+1} x_j + \sum_{k=0}^{n} (-1)^k D_k(\eta_k)$$
in $\mathcal{O}(V)$.

Lean: `GlobalTheory.T.projective_chart_affine_coords` (also `GlobalTheory.CompanionTheory.ConeTransfer.main`, the same statement).

In terms of forms, the left side is the coefficient of $d\log g_0 \wedge \dots \wedge d\log g_n$, and $\sum_k (-1)^k D_k(\eta_k)$ is the coefficient of $d\bigl(\sum_k \eta_k \, dt_0 \wedge \dots \widehat{dt_k} \dots \wedge dt_n\bigr)$. So the theorem says that $\pm d\log g_0 \wedge \dots \wedge d\log g_n$ is, on $V$, a sum of top forms that extend to the $U_{\hat \jmath}$ plus an exact form of an $n$-form that extends to $U_{\mathrm{all}}$.

**Remark 8.6.5.** The Lean statement carries three hypotheses, each a proposition proved elsewhere in the code: a local computation of graded pieces on a frame, a transfer statement for polynomial rings, and the [vanishing on affine opens](/entry/affine-graded-cohomology-vanishing/). They enter only through the local lemmas on $V$ in steps 6 and 7 below. The name of the theorem speaks of affine coordinates on a projective chart; the statement is the transfer lemma above. The Lean file imports Mathlib twice ([ProjectiveChartAffineCoordsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ProjectiveChartAffineCoordsStatement.lean#L1)).

The thickenings in the hypothesis are those of a site adapted to the cover. Let $W_j = i^{-1} D_+(X_j)$ be the standard charts of $\mathbb{P}^N$ pulled back to $X$. A thickening $T$ is in the adapted site over $U_S$ if, for each $k \in S$, the point of $T$ lies in $U_k \cap W_j$ for some $j$. The proof first moves everything to the simpler site $\mathcal{T}_{n+2}(U_{\mathrm{all}})$ of all thickenings over $U_{\mathrm{all}}$ with $J^{[n+2]} = 0$.

*Proof.*

1. *Change of site.* For $S = $ everything and for each $S = \{0, \dots, n+1\} \setminus \{j\}$, the restriction from $\mathcal{T}_{n+2}(U_S)$ to the adapted site over $U_S$ is bijective on $H^{n+1}(\operatorname{gr}^{n+1})$, and on $H^n(\operatorname{gr}^n)$ for $U_{\mathrm{all}}$. This is a lemma of the folder that compares the Zariski site with its refinement.
2. *The class $c'$.* On $\mathcal{T}_{n+2}(U_{\mathrm{all}})$, each $g_k$ lifts to a unit on every thickening, since the kernel of $B \to B/J$ is nilpotent. The truncated logarithms of these lifts are cocycles with values in $J$. Their cup product represents a class $c'$ in $H^{n+1}(\operatorname{gr}^{n+1})$. The restriction of $c'$ to the adapted site is represented by the same cochain as $c_0$. A class is determined by a representing cochain, so $c_0 = c'|$.
3. *The classes $\omega'_j$.* By step 1 each $\omega_j$ is the restriction of a class $\omega'_j$ on $\mathcal{T}_{n+2}(U_{\hat \jmath})$.
4. *The cochain $f'$.* A lifting lemma for exact sequences of filtered cochains gives an $n$-cochain $f'$ on $\mathcal{T}_{n+2}(U_{\mathrm{all}})$ with values in $J^{[n]}$, with $df'$ in $J^{[n+1]}$, which restricts to $f$ up to the bijection of step 1. Let $x_f$ be the class represented by $df'$.
5. *Gluing.* The classes $c'$ and $\sum_j \omega'_j|_{U_{\mathrm{all}}} + x_f$ have the same restriction to the adapted site, by steps 2 to 4 and the hypothesis on $f$. Restriction is injective by step 1. So
$$c' = \sum_j \omega'_j|_{U_{\mathrm{all}}} + x_f.$$
6. *Reading on $V$.* Restrict to the thickenings over $V$. Three local lemmas on $V$ compute the three terms in the form $x \, dt_0 \wedge \dots \wedge dt_n$, that is, as the class represented by the coefficient $x \in \mathcal{O}(V)$:
   - $c'|_V$ is represented by $(\prod_k g_k)^{-1} \det(D_k g_l)$, up to a sign;
   - $\omega'_j|_V$ is represented by a Jacobian form $x_j$ of $U_{\hat \jmath}$;
   - $x_f|_V$ is represented by $\sum_k (-1)^k D_k(\eta_k)$ with Jacobian forms $\eta_k$ of $U_{\mathrm{all}}$ of type "skip $k$".
7. *Uniqueness on $V$.* A lemma on the top chart says that the representation of a class of $H^{n+1}(\operatorname{gr}^{n+1})$ on $V$ by a coefficient $x$ is unique. Comparing the two representations of $c'|_V$ from steps 5 and 6 gives the identity. $\square$

**Remark 8.6.6.** The sign $\pm$ comes from the order of the factors in the cup product of $d\log$ classes against the order of the coordinates. The Lean statement keeps both signs as a disjunction and does not decide which one holds. The consumer only needs the identity up to sign.

**Remark 8.6.7.** The Lean proof raises the limit on elaboration steps to $1.6 \cdot 10^6$ ([ProjectiveChartAffineCoords.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ProjectiveChartAffineCoords.lean#L138)). We have read the statements of the lemmas cited in steps 1 to 7, not their proofs. The sites, the filtration and the frames on which the local lemmas rest are not unfolded here.

The theorem is passed on unchanged as [the transfer lemma](/entry/cone-transfer/) of the comparison chapter. There it is the last step of [the residue argument](/entry/pow-k-ne-zero-of/) that proves that the top power of the first Chern class is nonzero.
