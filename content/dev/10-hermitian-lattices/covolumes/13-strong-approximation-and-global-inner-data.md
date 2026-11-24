---
title: Strong approximation and global inner data
decls:
  - GlobalTheory.T.strong_approximation_unipotent_alt
  - GlobalTheory.T.globalInnerDatum_eq_iff_local_data_eq
  - GlobalTheory.Unfold.InnerDict.gdat_eq_iff
  - GlobalTheory.T.rationalClass_lattices_iff_rationalClass_localFramePairs
  - GlobalTheory.Unfold.ratCls_agree
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Strong approximation and global inner data

The next sections compute the sum of the squared row weights of the terms over one genus of local data. The answer is a mass: a sum over rational classes of local data of the inverse orders of their stabilizers. This section prepares the comparison of the two sides. First we state strong approximation for the unipotent groups $N$ and $N'$; it was used in [the theorem on rational witnesses](/entry/global-witnesses/). Then we attach to a lattice its global inner datum, and we show that this datum and the local data over the lattice determine each other. The last result says that rational classes of lattices and rational classes of local data are the same, with the same stabilizers. These results are used in the [orbit count](/entry/orbit-count/) and in the [mass identity](/entry/weights-add-up-to-mass-of/) of the next two sections.

**Theorem 2.13.1 (Strong approximation for the unipotent radicals).** Keep the setting of [global Hermitian frames](/entry/global-witnesses/): a quadratic extension $E/F$ of number fields, global frames $(S_p)_p$ with the groups $N_p$, $N'_p$ at the places $p$, and the global groups $N$, $N'$. Let $\Lambda$ be a lattice in $E^n$. Let $c_p \in F_p^\times$ be a family of scalars that are units for all but finitely many $p$. Let $n_p \in \mathrm{GL}(E_p^n)$ be a family with $n_p \Lambda_p = \Lambda_p$ for all but finitely many $p$.

1. If $n_p \in N_p$ for every $p$, then there is $g \in N$ such that, for every $p$, every $E_p$-linear map $g'$ that extends $g$ at $p$, and every $x \in \Lambda_p$, we have $n_p^{-1} g' x - x \in c_p \Lambda_p$.
2. The same holds with $N_p$, $N$ replaced by $N'_p$, $N'$.

Lean: `GlobalTheory.T.strong_approximation_unipotent_alt`.

*Proof.* This is the strong approximation theorem for the unipotent radical of the flag, proved for both flags by one argument. We sketch it for $N$. Let $X_0, \dots, X_{r-1}$ and $Y_0, \dots, Y_{r-1}$ be global vectors whose images at $p$ are $c_p^{r-a}$ times the flag and dual vectors of $S_p$; they satisfy $h(X_a, Y_b) = \delta_{ab}$ and $h(X_a, X_b) = h(Y_a, Y_b) = 0$. A local element of $N_p$ is an ordered product of Eichler isometries
$$E(X, u, s)\colon v \mapsto v + h(v, u) X - h(v, X)(u + s X),$$
with $X = X_i$, $u$ orthogonal to $X_a$ and $Y_a$ for $a \le i$, and $s + \bar s = h(u, u)$. Outside a finite set of places, $c_p$ is a unit, $\Lambda_p$ is the standard lattice and the local parameters $(u, s)$ are integral. At the remaining places choose $d_p$ so small that a change of the parameters by $d_p \mathcal{O}_p$ moves the product by an element that is $c_p$-close to the identity on $\Lambda_p$; this uses the continuity of the Eichler product on lattices. The approximation theorem for $E$ gives global parameters $(u_i, s_i)$ with the same orthogonality relations and $s_i + \bar s_i = h(u_i, u_i)$, within $d_p$ of the local ones at every $p$. The product $g$ of the global Eichler isometries lies in $N$, and it has the stated property at every place. $\square$

### The setting of semilocal frames

For the rest of this chapter we work in the following setting. Let $E$ be a number field with an involution $x \mapsto \bar x$, with fixed field $F$, and let $\mathcal{O}_E$ be its ring of integers. Let $V$ be an $E$-vector space of dimension $n = k + 2r + 1$ with a nondegenerate Hermitian form $h$, and let $g \ge 1$ be an integer, the level. A *frame* $F$ with parameter $T \in E$ is a flag frame $f_0, \dots, f_r$ in $V$ of the kind of [Section 2.11.5](/entry/global-witnesses/), together with an auxiliary vector. Write $X_F$ for the span of $f_0, \dots, f_{r-1}$; it is totally isotropic, so $X_F \subseteq X_F^\perp$. An isometry $\gamma$ is *adapted* from $F$ to $G$ if $\gamma f_a(F) - f_a(G)$ lies in the $a$-th step of the flag of $G$ for every $a$.

We fix two frames $F$ and $F'$ with parameters $T, T' \in \mathbb{N}$. We assume that the [[Gram matrix|00SPJSDT3Z]] of the pair is the matrix of a fixed point $w$, and that the invariant of the pair built from its minors is nonzero, as in [Section 2.11.5](/entry/global-witnesses/). At each finite place $p$ we fix a local Hermitian space $V_p = V \otimes E_p$ and a local frame pair $(A_p, B_p)$. The pair is *based* on $(F, F')$: the frame vectors of $A_p$ are the images of the $f_a(F)$, scaled by a fixed factor, the same for $B_p$ and $F'$, and the parameters of $A_p$ and $B_p$ are $T$ and $T'$. We also assume that each local frame pair is relevant at its value $\theta_p$, as in [Section 2.11.5](/entry/global-witnesses/). We call these the *standing assumptions*.

**Definition 2.13.2 (Global inner datum).** Let $\Lambda$ be an $\mathcal{O}_E$-lattice in $V$ and $F$ a frame. The *inner preimage* of $\Lambda$ at $F$ is
$$L_F(\Lambda) = \big((\Lambda \cap X_F^\perp) + X_F\big) \cap X_F^\perp.$$
It is the preimage in $X_F^\perp$ of the image of $\Lambda \cap X_F^\perp$ in $X_F^\perp / X_F$. Put $N_g(\Lambda) = g\Lambda + (\Lambda \cap X_F) + (\Lambda \cap X_{F'})$. The *graph set* $\Gamma(\Lambda)$ is the set of pairs $(p_1, p_2) \in V^2$ for which there are $l' \in \Lambda \cap X_{F'}^\perp$ and $l \in \Lambda \cap X_F^\perp$ with
$$p_1 - l' \in X_{F'}, \quad p_2 - l \in X_F, \quad l - l' \in N_g(\Lambda).$$
The *global inner datum* of $\Lambda$ is the triple
$$\operatorname{gdat}(\Lambda) = \big(L_F(\Lambda), L_{F'}(\Lambda), \Gamma(\Lambda)\big).$$

The first two entries remember the inner lattices of $\Lambda$ at the two flags. The graph set records how the two inner lattices are glued modulo $g$. It is the global form of the local datum $(L, L', \iota)$.

**Definition 2.13.3 (Rational classes of lattices).** Let $H_0(F, F')$ be the group of isometries of $(V, h)$ that fix every frame vector of $F$ and of $F'$. Two lattices $\Lambda_1$, $\Lambda_2$ are *rationally related*, $\Lambda_1 \sim \Lambda_2$, if some $\eta \in H_0(F, F')$ has $\operatorname{gdat}(\eta \Lambda_1) = \operatorname{gdat}(\Lambda_2)$. The *stabilizer* of $\Lambda$ is
$$\operatorname{Stab}(\Lambda) = \{\eta \in H_0(F, F') : \operatorname{gdat}(\eta \Lambda) = \operatorname{gdat}(\Lambda)\}.$$

**Definition 2.13.4 (Families of local data).** A *family of local data* is a family $y = (y_p)_p$ with $y_p = (L_p, L'_p, \iota_p)$ a datum for the local frame pair $(A_p, B_p)$. Here $L_p$ and $L'_p$ are inner lattices in the reduced spaces $X^\perp/X$ of the two local frames, and $\iota_p$ is a set that is empty unless $p$ splits in $E$. A local map $\eta'$ of $V_p$ *extends* a global map $\eta$ if $\eta'(x \otimes 1) = (\eta x) \otimes 1$ for all $x \in V$. A global $\eta$ *moves* $y$ to $y'$ if at every $p$ some extension of $\eta$ moves $y_p$ to $y'_p$. Two families are *rationally related*, $y \approx y'$, if some $\eta \in H_0(F, F')$ moves $y$ to $y'$. The *stabilizer* $\operatorname{Stab}(y)$ is the set of $\eta \in H_0(F, F')$ that move $y$ to itself. A lattice $\Lambda$ *lies over* $y$ if $\Lambda$ is a lattice and at every $p$ there is a local term over $y_p$ whose lattice is $\Lambda_p$.

**Proposition 2.13.5 (The global inner datum and the local data).** Under the standing assumptions, let $\Lambda_1$ lie over $y_1$ and $\Lambda_2$ lie over $y_2$. Then $\operatorname{gdat}(\Lambda_1) = \operatorname{gdat}(\Lambda_2)$ if and only if $y_1 = y_2$.

Lean: `GlobalTheory.Unfold.InnerDict.gdat_eq_iff` (also `GlobalTheory.T.globalInnerDatum_eq_iff_local_data_eq`, a second name).

*Proof.* A local datum is determined by its three entries, so we compare the entries one at a time. For a local term over $y_{i,p}$, the inner lattice $L_{i,p}$ is the image of $\Lambda_{i,p} \cap X^\perp$ in $X^\perp/X$; this is the identification of the datum lattice of a term with the perp quotient image of its lattice. Since the local frames are based on $F$ and $F'$, this image is the localization of the global inner preimage $L_F(\Lambda_i)$. So $L_F(\Lambda_1) = L_F(\Lambda_2)$ gives $L_{1,p} = L_{2,p}$ at every $p$. Conversely, a lattice in $V$ is determined by its localizations, so equal local inner lattices at all $p$ give equal inner preimages. The same holds at $F'$. For the third entry, assume that the inner preimages agree at both frames. At a split place, the set $\iota_p$ is the graph of the local identification of the two reduced lattices modulo $g$. If the global graph sets agree, the local identifications agree at every split place; conversely, if they agree at every split place, the global graph sets agree. At a place that does not split, $\iota_{1,p}$ and $\iota_{2,p}$ are both empty. Together these steps give both directions. $\square$

**Theorem 2.13.6 (Rational classes of lattices and of local data).** Under the standing assumptions:

1. the relation $\approx$ on families of local data is an equivalence relation;
2. if $y \approx y'$, then $\#\operatorname{Stab}(y) = \#\operatorname{Stab}(y')$, as elements of $\mathbb{N} \cup \{\infty\}$;
3. if $\Lambda_1$ lies over $y_1$ and $\Lambda_2$ lies over $y_2$, then $\Lambda_1 \sim \Lambda_2$ if and only if $y_1 \approx y_2$, and $\operatorname{Stab}(\Lambda_1) = \operatorname{Stab}(y_1)$.

Lean: `GlobalTheory.Unfold.ratCls_agree` (also `GlobalTheory.T.rationalClass_lattices_iff_rationalClass_localFramePairs`, a second name).

*Proof.* The group $H_0(F, F')$ contains $1$ and is closed under products and inverses. The extension relation is compatible with these: $1$ extends $1$, $\eta' \zeta'$ extends $\eta \zeta$, and $\eta'^{-1}$ extends $\eta^{-1}$. The local groups act on local data, so moving is compatible with products and inverses. This gives reflexivity, symmetry and transitivity of $\approx$, which is (1). For (2), if $\zeta$ moves $y$ to $y'$, then conjugation $\eta \mapsto \zeta \eta \zeta^{-1}$ is a bijection from $\operatorname{Stab}(y)$ to $\operatorname{Stab}(y')$. For (3), let $\eta \in H_0(F, F')$ and let $\eta'$ extend $\eta$ at $p$. A rational isometry that fixes both frames moves the local lattices of a term to the local lattices of the moved term: $\eta' \Lambda_p = (\eta \Lambda)_p$, and the local term over $y_p$ with lattice $\Lambda_p$ goes to a local term over $\eta' y_p$ with lattice $(\eta\Lambda)_p$. So $\eta\Lambda_1$ lies over the family $\eta y_1$. By the [Proposition 2.13.5](/entry/gdat-eq-iff/), $\operatorname{gdat}(\eta \Lambda_1) = \operatorname{gdat}(\Lambda_2)$ holds if and only if $\eta y_1 = y_2$. This proves both the equivalence of the relations and, with $\Lambda_2 = \Lambda_1$, the equality of stabilizers. $\square$

**Remark 2.13.7 (Formalization).** The strong approximation theorem is a wrapper of `GlobalTheory.HL.SAN.strong_approximation_unipotent` ([StrongApproximationUnipotent.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/StrongApproximationUnipotent.lean#L309)); its main work is the lemma `core` at line 50 of that file. The lemma named `principalPolarisation_exists_unique_section` only proves $1 \in H_0(F, F')$; its name has nothing to do with its content ([RationalClassLatticesIffRationalClassLocalFrameP.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RationalClassLatticesIffRationalClassLocalFrameP.lean#L21)). The stabilizer sizes are `Set.encard`, so an infinite stabilizer has size $\infty$. The conditions on the flags in the frame (`IsLift`, the convolution condition) are not unfolded here.
