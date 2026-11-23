---
title: Homological stability for general linear groups
decls:
  - GlobalTheory.HomStab.kStability_main
  - PositivityTheory.v8.KStability.kStability
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Homological stability for general linear groups

This section proves that the integral homology of $\mathrm{GL}_n(R)$ does not change when $n$ grows past a bound that is linear in the degree. The ring $R$ is any commutative ring of finite stable range. The result is a published theorem that [Lemma K](/entry/lemma-k-lit-n-alt/) takes as an input, and the window bound uses Lemma K in [step 5](/proof/vwin/). The proof is Quillen's argument: the group acts on the complex of split sequences of the [previous section](/entry/split-seq-exact-at-of-two-mul-add-stable-range-le/), and a spectral sequence compares its homology in low degrees with the homology of the smaller groups. The background is in [general linear groups](/learn/groups/#general-linear-and-symplectic-groups).

### Group homology and the stabilization maps

For a group $G$ and $i \ge 0$, write $H_i(G) = H_i(G; \mathbb{Z})$ for the homology of $G$ with coefficients in $\mathbb{Z}$ with the trivial action. A homomorphism $\phi \colon G \to G'$ induces $\phi_* \colon H_i(G) \to H_i(G')$. For a $G$-module $M$ we write $H_i(G; M)$ for homology with coefficients in $M$.

**Definition 7.2.1 (Stabilization map).** Let $R$ be a commutative ring and $m \le m'$. The *stabilization map* $\iota_{m,m'} \colon \mathrm{GL}_m(R) \to \mathrm{GL}_{m'}(R)$ sends $g$ to the block matrix
$$\iota_{m,m'}(g) = \begin{pmatrix} g & 0 \\ 0 & 1_{m'-m} \end{pmatrix}.$$
Write $\iota_m = \iota_{m,m+1}$.

The map $\iota_{m,m'}$ is an injective homomorphism. The direct limit of the groups $\mathrm{GL}_m(R)$ along these maps is $\mathrm{GL}(R)$, and Quillen's plus construction turns its homology into the algebraic $K$-theory of $R$. Stability says that the limit is reached at a finite stage in each degree.

**Theorem 7.2.2 (Homological stability).** Let $R$ be a commutative ring of [stable range](/entry/split-acyclic-step/) at most $s$. Let $i, n \ge 0$ with $2i + s + 2 \le n$. Then
$$(\iota_n)_* \colon H_i(\mathrm{GL}_n(R); \mathbb{Z}) \to H_i(\mathrm{GL}_{n+1}(R); \mathbb{Z})$$
is an isomorphism.

Lean: `GlobalTheory.HomStab.kStability_main` (also `PositivityTheory.v8.KStability.kStability`, a second name).

### The first page

Fix $m$ and put $G = \mathrm{GL}_{m+1}(R)$. Let $S_p$ be the set of split sequences of length $p$ in $R^{m+1}$, and $C_p = \mathbb{Z}[S_p]$ the permutation module. Since $S_0$ has one element, $C_0 = \mathbb{Z}$ with the trivial action. The deletion differential makes $C_\bullet$ a complex of $G$-modules
$$\cdots \to C_2 \to C_1 \to C_0 = \mathbb{Z} \to 0.$$
Its homology is the homology of the complex $S(R^{m+1})$ of the previous section. So it vanishes at $p$ when $2p + s + 1 \le m + 1$.

Two facts identify the terms $H_q(G; C_p)$.

1. Transitivity. If $p + s \le m + 1$, then $G$ acts transitively on $S_p$. The proof moves a split sequence to the standard one, one pair at a time. The stable range condition is what allows the last coordinate of a unimodular vector to be cleared by elementary matrices.
2. Stabilizers. Let the standard split sequence of length $p$ use the last $p$ basis vectors and their dual forms. Its stabilizer in $G$ is the image of $\iota_{m+1-p, m+1}$: a matrix that fixes these vectors and forms is the identity on the last $p$ coordinates and preserves the complement.

By Shapiro's lemma, $H_q(G; \mathbb{Z}[G/H]) \cong H_q(H)$ for a subgroup $H$. So for $p + s \le m + 1$ there is an isomorphism
$$e_{p,q} \colon H_q(\mathrm{GL}_{m+1-p}(R)) \xrightarrow{\ \sim\ } H_q(G; C_p).$$
Under these isomorphisms the map $H_q(G; C_{p+1}) \to H_q(G; C_p)$ induced by the differential is $(\iota_{m-p})_*$ when $p$ is even and $0$ when $p$ is odd. The reason is that the $p + 1$ faces of the standard sequence of length $p + 1$ are conjugate to the standard sequence of length $p$ by elements that commute with the stabilizer, so each face contributes $(\iota_{m-p})_*$, with alternating signs, and the sum has $p + 1$ terms.

### The induction

*Proof of the theorem.* We prove by strong induction on $i$ the following pair of claims, for all $m$:

1. if $2i + s + 1 \le m$, then $(\iota_m)_* \colon H_i(\mathrm{GL}_m(R)) \to H_i(\mathrm{GL}_{m+1}(R))$ is surjective;
2. if $2i + s + 2 \le m$, then this map is injective.

Fix $i$ and assume both claims in all degrees $q < i$. Consider the hyperhomology of $G = \mathrm{GL}_{m+1}(R)$ with coefficients in the complex $C_\bullet$. One spectral sequence has $E^1_{p,q} = H_q(G; C_p)$ with $d^1$ induced by the differential of $C_\bullet$. The other is computed from the homology of $C_\bullet$, which vanishes in the range given by the [acyclicity theorem](/entry/split-seq-exact-at-of-two-mul-add-stable-range-le/). So the first spectral sequence converges to zero in low total degree. By the first page, $E^1_{p,q} \cong H_q(\mathrm{GL}_{m+1-p}(R))$ in the relevant range, and the differential $d^1 \colon E^1_{1,i} \to E^1_{0,i}$ is $(\iota_m)_*$ in degree $i$.

For surjectivity: $E^1_{0,i} = H_i(G)$ must die in the limit. The differentials $d^1$ out of the columns $p \ge 2$ into rows $q < i$ are stabilization maps between groups of smaller rank, and the induction hypothesis says that they are surjective or injective as needed, so that the rows $q < i$ contribute nothing that can hit $E_{0,i}$. Then $E^1_{0,i}$ must be the image of $d^1$ from $E^1_{1,i}$, which is surjectivity of $(\iota_m)_*$ in degree $i$. For injectivity one argues in the same way one degree higher. The kernel of $d^1 \colon E^1_{1,i} \to E^1_{0,i}$ must be killed by differentials from columns $p \ge 2$. The $d^1$ from $E^1_{2,i}$ is $0$, since $p = 1$ is odd, and the higher differentials come from rows $q < i$, where the induction hypothesis applies. The bounds $2i + s + 1 \le m$ and $2i + s + 2 \le m$ are those needed for the acyclicity theorem and for the transitivity statement in each step. These spectral sequence arguments are proved once, for an abstract complex of $G$-modules with the properties above, and then applied to $C_\bullet$.

The two claims together, for $n$ with $2i + s + 2 \le n$, show that $(\iota_n)_*$ is bijective in degree $i$, so it is an isomorphism. $\square$

**Remark 7.2.3.** Quillen proved stability for $\mathrm{GL}_n$ of a field with this kind of argument. Van der Kallen proved stability for rings of finite stable range, in a range linear in the degree. For the ring of integers $\mathcal{O}_L$ of a number field, stable range at most $2$ gives stability for $n \ge 2i + 4$. The [next sections](/entry/b-star-odd/) use the stable groups $H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L))$ for $n \ge 2(k+1) + 4$, which is the same bound.

**Remark 7.2.4 (Formalization).** The input statement is the definition `UpperTheory.V.Published.KStability`, which says exactly the theorem above for all commutative rings. The theorem `PositivityTheory.v8.KStability.kStability` is the same statement with the proof term `kStability_main`. The file [HomologicalStabilityTheorem.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/HomologicalStabilityTheorem.lean#L31) ends with an empty section that only opens namespaces. The surjective step is reached through a wrapper whose proof is `first | exact grpHMap_stab_surjective_step | exact grpHMap_stab_surjective_congr`, and the second branch cannot close the goal. The spectral sequence is not built as an object: the abstract lemma `quillen_stabilisation_surjective_bottom` and its injective twin work directly with the complex and the maps $e_{p,q}$. We have not unfolded these two lemmas, and the description of the spectral sequence above follows their hypotheses.
