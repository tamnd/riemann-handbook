---
title: Kodaira-Spencer maps and the rho-part count
decls:
  - GlobalTheory.T.harrisTaylor_rho_part_deformation_dim
  - GlobalTheory.HTRho.rhoCount
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kodaira-Spencer maps and the rho-part count

The previous section reduced the relative dimension of a model to a count of first-order deformations of one object over an algebraically closed field. This section and the next do that count. A first-order deformation is fixed by a lift of the Hodge filtration, and such a lift is given by a linear map on de Rham homology with three properties: it commutes with the action of $O$ up to the filtration, it respects a Lie subspace, and it is skew for the polarization pairing. We call these maps Kodaira-Spencer maps. Here we define them and count them, up to the filtration, for an auxiliary filtration and the zero pairing. The answer is $a(n - 1)$. The next section passes from this count to the filtration $\operatorname{Fil}(A_0)$ and the polarization pairing, in [the theorem on Kodaira-Spencer directions](/entry/ks-dim-at-point/).

### Kodaira-Spencer maps

Let $k$ be a field, $H$ a $k$-vector space, $O$ a ring and $\sigma : O \to \operatorname{End}_k(H)$ a ring map. Let $\operatorname{Fil}$ and $Z$ be subspaces of $H$ and $\varphi$ a bilinear form on $H$.

**Definition 8.20.1 (Kodaira-Spencer map).** A linear map $f : H \to H$ is a *Kodaira-Spencer map* for $(\sigma, \varphi, \operatorname{Fil}, Z)$ if the following hold.

1. $f(\sigma(a) x) - \sigma(a) f(x) \in \operatorname{Fil}$ for all $a \in O$ and $x \in \operatorname{Fil}$.
2. $f(Z) \subseteq \operatorname{Fil}$.
3. $\varphi(f x, y) + \varphi(x, f y) = 0$ for all $x, y \in \operatorname{Fil}$.

Lean: `GlobalTheory.UPel.Sm.IsKS`.

The three conditions are linear in $f$, so the Kodaira-Spencer maps form a subspace of $\operatorname{End}_k(H)$. Only the map $\operatorname{Fil} \to H/\operatorname{Fil}$, $x \mapsto f x \bmod \operatorname{Fil}$, matters for filtration lifts. So we count Kodaira-Spencer maps up to maps that send $\operatorname{Fil}$ into $\operatorname{Fil}$.

**Definition 8.20.2 (Kodaira-Spencer dimension).** Let $d \geq 0$. We say that $(\sigma, \varphi, \operatorname{Fil}, Z)$ has *Kodaira-Spencer dimension* $d$ if there are Kodaira-Spencer maps $f_1, \dots, f_d$ with this property: for every Kodaira-Spencer map $g$ there are unique $c_1, \dots, c_d \in k$ such that $g x - \sum_i c_i f_i x \in \operatorname{Fil}$ for all $x \in \operatorname{Fil}$.

Lean: `GlobalTheory.UPel.Sm.KSDim`.

**Lemma 8.20.3 (The Kodaira-Spencer dimension is a dimension).** Let $H$ be finite-dimensional. Let $M \subseteq \operatorname{Hom}_k(\operatorname{Fil}, H/\operatorname{Fil})$ be the image of the space of Kodaira-Spencer maps under $f \mapsto (x \mapsto f x \bmod \operatorname{Fil})$. Then $(\sigma, \varphi, \operatorname{Fil}, Z)$ has Kodaira-Spencer dimension $\dim M$.

Lean: `GlobalTheory.UPel.Sm.KSCount.ksDim_finrank`.

*Proof.* Choose a basis of $M$ and Kodaira-Spencer maps $f_1, \dots, f_d$ whose images are the basis vectors. Let $g$ be a Kodaira-Spencer map. The condition $g x - \sum_i c_i f_i x \in \operatorname{Fil}$ for all $x \in \operatorname{Fil}$ says that the image of $g$ in $M$ equals $\sum_i c_i$ times the $i$-th basis vector. So $c$ exists and is unique. $\square$

### Augmentation and Lie subspaces

Now let $C$ be a commutative ring and let $O$ be a $C$-algebra. For $c \in C$ we write $\sigma(c)$ for $\sigma$ of the image of $c$ in $O$. As $C$ maps into the center of $O$, each $\sigma(c)$ commutes with each $\sigma(a)$.

**Definition 8.20.4 (Augmentation subspace, Lie subspace, equivariant maps).** Let $X \subseteq H$ be a subspace.

1. For a ring map $\chi : C \to k$, the *augmentation subspace* $X_\chi$ is the span of the vectors $\sigma(c) x - \chi(c) x$ with $c \in C$ and $x \in X$.
2. For a family $\chi = (\chi_i)_{i \in I}$ of ring maps $C \to k$, the *Lie subspace* $J_\chi(X)$ is the span of the vectors $\sum_l \lambda_l \sigma(c_l) x$, where $x \in X$, $\lambda_1, \dots, \lambda_r \in k$ and $c_1, \dots, c_r \in C$ satisfy $\sum_l \lambda_l \chi_i(c_l) = 0$ for every $i$.
3. For $k$-spaces $X$ and $Y$ with ring maps $O \to \operatorname{End}_k(X)$ and $O \to \operatorname{End}_k(Y)$, $\operatorname{Hom}_O(X, Y)$ is the space of $k$-linear maps $X \to Y$ that commute with $O$.

Lean: `GlobalTheory.HTRho.mSub`, `GlobalTheory.HTRho.jSub`, `GlobalTheory.HTRho.homO`.

The quotient $H/H_\chi$ is the largest quotient of $H$ on which $C$ acts through $\chi$. If $J_\chi(H) = 0$, then $\sigma(c)$ is a linear function of the vector $(\chi_i(c))_{i \in I}$, so $C$ acts on $H$ only through the characters $\chi_i$. For an $O$-stable subspace $X$ we give $X$, $H/X$ and their quotients the induced actions.

### Inputs

We use the following results. In results 1 to 5, $H$, $W$ and $V$ are finite-dimensional $k$-spaces with ring maps from $O$, and $\chi = (\chi_i)_{i \in I}$ is a family of ring maps $C \to k$ indexed by a finite set $I$.

1. (Zero pairing.) Let $G$ and $Z$ be $O$-stable subspaces of $H$ with $Z \subseteq G$. Then the image of the space of Kodaira-Spencer maps for $(\sigma, 0, G, Z)$ in $\operatorname{Hom}_k(G, H/G)$ has dimension $\dim \operatorname{Hom}_O(G/Z, H/G)$.
2. (Splitting by characters.) If $\chi$ is injective and $J_\chi(V) = 0$, then $\dim \operatorname{Hom}_O(W, V) = \sum_{i \in I} \dim \operatorname{Hom}_O(W, V/V_{\chi_i})$.
3. (Scalar target.) If $C$ acts on $V$ through $\chi_i$, then $\dim \operatorname{Hom}_O(W, V) = \dim \operatorname{Hom}_O(W/W_{\chi_i}, V)$.
4. (Quotients.) Let $G \subseteq H$ be $O$-stable. If $J_\chi(H) \subseteq G$, then $J_\chi(H/G) = 0$. For each $i$, $\dim (H/G)/(H/G)_{\chi_i} = \dim H/(G + H_{\chi_i})$.
5. (Two roots.) Let $\chi$ be injective, $\operatorname{Fil} \subseteq H$ an $O$-stable subspace, $\omega \in C$ and $r_0 \neq r_1$ in $k$ with $(\sigma(\omega) - r_0)(\sigma(\omega) - r_1) = 0$ and $\chi_i(\omega) = r_0$ for all $i$. Put $G = \operatorname{Fil} + \operatorname{im}(\sigma(\omega) - r_0)$ and $Z = J_\chi(\operatorname{im}(\sigma(\omega) - r_1))$. Suppose that $G$ and $Z$ are $O$-stable and $J_\chi(H) \subseteq G$. Then for each $i$, with $W = G/Z$,
$$\dim W/W_{\chi_i} + \dim H/(G + H_{\chi_i}) = \dim H/H_{\chi_i}.$$

### The abstract count

**Lemma 8.20.5 (Count with two roots).** Let $H$ be finite-dimensional, $I$ a finite set and $\chi = (\chi_i)_{i \in I}$ an injective family of ring maps $C \to k$. Let $\operatorname{Fil} \subseteq H$ be $O$-stable. Let $\omega \in C$ and $r_0 \neq r_1$ in $k$ with $(\sigma(\omega) - r_0)(\sigma(\omega) - r_1) = 0$ and $\chi_i(\omega) = r_0$ for all $i$. Let $m > 0$ and $n$ be integers. Put $G = \operatorname{Fil} + \operatorname{im}(\sigma(\omega) - r_0)$ and $Z = J_\chi(\operatorname{im}(\sigma(\omega) - r_1))$. Assume:

1. $\dim H/H_{\chi_i} = mn$ for each $i$;
2. $J_\chi(H) \subseteq G$;
3. $\dim H/(G + H_{\chi_i}) = m$ for each $i$;
4. for each $i$ and all finite-dimensional $X$, $Y$ with actions of $O$ on which $C$ acts through $\chi_i$, $m^2 \dim \operatorname{Hom}_O(X, Y) = \dim X \cdot \dim Y$.

Then $(\sigma, 0, G, Z)$ has Kodaira-Spencer dimension $|I|(n - 1)$.

Lean: `GlobalTheory.HTRho.count`.

*Proof.* As $\sigma(\omega)$ commutes with $O$, the images of $\sigma(\omega) - r_0$ and $\sigma(\omega) - r_1$ are $O$-stable, so $G$ is $O$-stable. The same argument shows that $Z$ is $O$-stable. Also $Z \subseteq J_\chi(H) \subseteq G$ by assumption 2. By the previous lemma and result 1, the Kodaira-Spencer dimension of $(\sigma, 0, G, Z)$ is $\dim \operatorname{Hom}_O(W, H/G)$ with $W = G/Z$. By result 4 and assumption 2, $J_\chi(H/G) = 0$. Result 2 gives
$$\dim \operatorname{Hom}_O(W, H/G) = \sum_{i \in I} \dim \operatorname{Hom}_O(W, V_i), \qquad V_i = (H/G)/(H/G)_{\chi_i}.$$
By result 4 and assumption 3, $\dim V_i = m$. The ring $C$ acts on $V_i$ through $\chi_i$, so result 3 gives $\dim \operatorname{Hom}_O(W, V_i) = \dim \operatorname{Hom}_O(W/W_{\chi_i}, V_i)$. By result 5 and assumptions 1 and 3, $\dim W/W_{\chi_i} = mn - m$. Now $C$ acts on both $W/W_{\chi_i}$ and $V_i$ through $\chi_i$, and assumption 4 gives $m^2 \dim \operatorname{Hom}_O(W/W_{\chi_i}, V_i) = m(n - 1) \cdot m$. As $m > 0$, this dimension is $n - 1$. Summing over $I$ gives $|I|(n - 1)$. $\square$

### The count at a point

Fix a datum $D$, a base $b$ over $R$ (Definitions 8.1.1 and 8.1.2), an integer $N \geq 3$ prime to $p$, and an algebraically closed field $k$. Let $o_0$ be an object of level $N$ over $t : \operatorname{Spec} k \to \operatorname{Spec} R$ (Definition 8.1.3), with abelian variety $A_0$, and let $\beta : R \to k$ be a ring map with $t = \operatorname{Spec} \beta$. We use $H(A_0)$ and $\operatorname{Fil}(A_0)$ from the previous section.

**Definition 8.20.6 (Crystalline action and Lie subspace at a point).** The *crystalline action* $\sigma_0 : O \to \operatorname{End}_k H(A_0)$ sends $a$ to the map that the endomorphism $a$ of $A_0$ induces on $H(A_0)$, the dual of its pullback on primitive de Rham classes. Put $r = \beta(\rho)$, where $\rho$ is the root of the base, and $\chi_i = \beta \circ t_i : \mathcal{O}_F \to k$ for $i = 1, \dots, a$. The *Lie subspace* of $o_0$ at $\beta$ is
$$Z(o_0, \beta) = J_\chi\big(\operatorname{im}(\sigma_0(\omega) - (t_0 - r))\big),$$
with $C = \mathcal{O}_F$ acting on $H(A_0)$ through $\mathcal{O}_F \to O$.

Lean: `GlobalTheory.HTCount.crysAct` (also `GlobalTheory.HTCount.rhoPart` for the image of $\sigma_0(\omega) - (t_0 - r)$, and `GlobalTheory.HTCount.lieZ`).

We use the following results about $o_0$, with $H = H(A_0)$ and $G_0 = \operatorname{Fil}(A_0) + \operatorname{im}(\sigma_0(\omega) - r)$.

6. (Finiteness.) $H$ is finite-dimensional.
7. (Stability.) For every endomorphism of $A_0$, the induced map on $H$ preserves $\operatorname{Fil}(A_0)$. In particular $\operatorname{Fil}(A_0)$ is $O$-stable.
8. (The Lie quotient.) $J_\chi(H) \subseteq G_0$, and $\dim H/(G_0 + H_{\chi_i}) = m$ for each $i$.
9. (The character quotient.) $\dim H/H_{\chi_i} = mn$ for each $i$.
10. (A Morita count.) Let $k$ be an algebraically closed field in which every integer prime to $p$ is nonzero. Let $\chi : \mathcal{O}_F \to k$ be a ring map, and let $X$, $Y$ be finite-dimensional $k$-spaces with ring maps from $O$ on which $\mathcal{O}_F$ acts through $\chi$. Then $m^2 \dim \operatorname{Hom}_O(X, Y) = \dim X \cdot \dim Y$.

Result 10 is the shadow of the isomorphism $O \otimes \mathbb{Z}_p \cong M_m(\mathcal{O}_F \otimes \mathbb{Z}_p)$ in Definition 8.1.1: modules over a matrix algebra $M_m(k)$ are sums of copies of $k^m$.

**Theorem 8.20.7 (The rho-part count).** Let $o_0$ be an object of level $N$ over $t = \operatorname{Spec} \beta$ as above. Then $(\sigma_0, 0, \operatorname{Fil}(A_0) + \operatorname{im}(\sigma_0(\omega) - \beta(\rho)), Z(o_0, \beta))$ has Kodaira-Spencer dimension $a(n - 1)$.

Lean: `GlobalTheory.HTRho.rhoCount` (also `GlobalTheory.T.harrisTaylor_rho_part_deformation_dim`, a second name).

*Proof.* We apply the lemma on the count with two roots, with $C = \mathcal{O}_F$, $I = \{1, \dots, a\}$, $\chi_i = \beta t_i$, $\operatorname{Fil} = \operatorname{Fil}(A_0)$, $r_0 = r = \beta(\rho)$, $r_1 = t_0 - r$, and $m$, $n$ from the datum. Then $G = G_0$ and $Z = Z(o_0, \beta)$. We check its hypotheses.

$H$ is finite-dimensional by result 6, and $\operatorname{Fil}(A_0)$ is $O$-stable by result 7. The family $\chi$ is injective. Indeed, if $\chi_i = \chi_j$ with $i \neq j$, then $\beta$ kills every $t_i(x) - t_j(x)$. These elements generate the unit ideal of $R$ (Definition 8.1.2), so $\beta(1) = 0$, which is false. Next, $\chi_i(\omega) = \beta(t_i(\omega)) = \beta(\rho) = r$.

The two roots differ. As $\rho$ is a root of $X^2 - t_0 X + n_0$, so is $r$ in $k$, and $(2r - t_0)^2 = t_0^2 - 4n_0$. If $r = t_0 - r$, then $t_0^2 - 4n_0 = 0$ in $k$. But $p \nmid t_0^2 - 4n_0$, so $|t_0^2 - 4n_0|$ is an integer prime to $p$. It is a unit in $R$ by Definition 8.1.2, so it is nonzero in $k$. This is a contradiction.

The quadratic relation. From $\omega + \bar\omega = t_0$ and $\omega \bar\omega = n_0$ we get $\omega^2 - t_0 \omega + n_0 = 0$ in $\mathcal{O}_F$. So $\sigma_0(\omega)^2 - t_0 \sigma_0(\omega) + n_0 = 0$. As $r + (t_0 - r) = t_0$ and $r(t_0 - r) = n_0$, this is $(\sigma_0(\omega) - r)(\sigma_0(\omega) - (t_0 - r)) = 0$.

We have $m > 0$ by Definition 8.1.1. Assumptions 1, 2 and 3 of the lemma are results 9 and 8. Assumption 4 is result 10: every integer prime to $p$ is a unit in $R$, so it is nonzero in $k$. The lemma gives the Kodaira-Spencer dimension $a(n - 1)$. $\square$

**Remark 8.20.8 (Formalization).** The second name is a wrapper that tries three forms of one proof term under a raised heartbeat limit: [HarrisTaylorRhoPartDeformationDimStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorRhoPartDeformationDimStatement.lean#L7). The theorem is in [HarrisTaylorRhoPartDeformationDim.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorRhoPartDeformationDim.lean#L157), and the lemma on the count with two roots in the same file at [line 98](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorRhoPartDeformationDim.lean#L98). The pairing in the theorem is the zero form, so condition 3 of a Kodaira-Spencer map is empty there. Result 10 is stated for spaces in one universe, and the proof moves to coordinates $k^{\dim X}$ to apply it. Two inputs live in files whose names say something else: result 5 is proved in [MonoidAlgebraActionViaRingActionApplyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MonoidAlgebraActionViaRingActionApplyStatement.lean#L7), and result 3 in [KodairaSpencerFormApplyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KodairaSpencerFormApplyStatement.lean#L7). The hypotheses $N \geq 3$ and $N$ prime to $p$ are passed on to results 8 and 9. We read the statements of results 1 to 10, not their proofs. The description of $\sigma_0$ in words is ours: it is the push of the action on de Rham homology, which we have not unfolded.
