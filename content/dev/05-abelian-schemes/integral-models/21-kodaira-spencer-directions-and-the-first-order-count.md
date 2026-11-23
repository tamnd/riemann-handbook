---
title: Kodaira-Spencer directions and the first-order count
decls:
  - GlobalTheory.HTCount.count
  - GlobalTheory.T.harrisTaylor_kodairaSpencer_directions_dim
  - GlobalTheory.HTCount.ksDim_at_point
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kodaira-Spencer directions and the first-order count

This section proves the theorem that the section on smoothness used for the relative dimension: an object of level $N$ over an algebraically closed field has exactly $a(n - 1)$ independent first-order deformations, each given by a lift of its Hodge filtration. The proof has two steps. First we pass from the count of [the previous section](/entry/rho-count/), which uses an auxiliary filtration and the zero pairing, to a count of Kodaira-Spencer maps for $\operatorname{Fil}(A_0)$ and the pairing of the polarization. The pairing is skew and nondegenerate and $\operatorname{Fil}(A_0)$ is Lagrangian, and this lets us trade one count for the other. Then we match Kodaira-Spencer maps with deformations.

Throughout, $D$ is a datum, $b$ a base over $R$, $N \geq 3$ an integer prime to $p$ and $k$ an algebraically closed field. Let $o_0$ be an object of level $N$ over $t : \operatorname{Spec} k \to \operatorname{Spec} R$, with abelian variety $A_0$ and line bundle $P$ on $A_0 \times A_0$, and let $\beta : R \to k$ with $t = \operatorname{Spec} \beta$. We use $H(A_0)$, $\operatorname{Fil}(A_0)$, filtration lifts and deformations from [the section on smoothness](/entry/htuniv-main/), and the crystalline action $\sigma_0$ and the Lie subspace $Z(o_0, \beta)$ from the previous section. Put $r = \beta(\rho)$ and $r' = t_0 - r$.

### The polarization pairing

**Definition 8.21.1 (Polarization pairing).** A bilinear form $\varphi$ on $H(A_0)$ is a *polarization pairing* of $o_0$ if there are primitive de Rham classes $a_1, \dots, a_s$ and $b_1, \dots, b_s$ of $A_0$ such that $\sum_j \operatorname{pr}_1^* a_j \cup \operatorname{pr}_2^* b_j$ is the de Rham Chern class of $P$ in the second de Rham cohomology of $A_0 \times A_0$, and
$$\varphi(x, y) = \sum_j x(a_j)\, y(b_j) \quad \text{for } x, y \in H(A_0).$$

Lean: `GlobalTheory.AbDual.IsCorrForm`.

So $\varphi$ is the Chern class of $P$, read as a form on the dual of the primitive classes.

### Inputs

We use the following results. Let $\varphi$ be a polarization pairing of $o_0$.

1. (Existence.) $o_0$ has a polarization pairing.
2. (Skew and Lagrangian.) $H(A_0)$ is finite-dimensional, $2 \dim \operatorname{Fil}(A_0) = \dim H(A_0)$, $\varphi(x, y) = -\varphi(y, x)$ for all $x, y$, and $\varphi(x, y) = 0$ for $x, y \in \operatorname{Fil}(A_0)$.
3. (Nondegenerate.) If $\varphi(x, y) = 0$ for all $y$, then $x = 0$.
4. (Adjoint.) $\varphi(\sigma_0(c) x, y) = \varphi(x, \sigma_0(c^*) y)$ for all $c \in O$ and $x, y \in H(A_0)$.
5. (Stability.) $\operatorname{Fil}(A_0)$ is $O$-stable.
6. (Reduction to an eigenspace.) Let $k$ be a field, $H$ a finite-dimensional $k$-space, $\sigma : O \to \operatorname{End}_k(H)$ a ring map and $s : O \to O$ a surjective map with $\varphi(\sigma(c) x, y) = \varphi(x, \sigma(s(c)) y)$. Let $\varphi$ be skew and nondegenerate, and let $\operatorname{Fil} \subseteq H$ be $O$-stable, isotropic for $\varphi$, with $2 \dim \operatorname{Fil} = \dim H$. Let $w \in O$ with $\sigma(w)$ central in the image of $\sigma$, and $r \neq r'$ in $k$ with $(\sigma(w) - r)(\sigma(w) - r') = 0$ and $\varphi(\sigma(w) x, y) = \varphi(x, (r + r') y - \sigma(w) y)$. Let $Z \subseteq \operatorname{im}(\sigma(w) - r')$. If $(\sigma, 0, \operatorname{Fil} + \operatorname{im}(\sigma(w) - r), Z)$ has Kodaira-Spencer dimension $d$, then $(\sigma, \varphi, \operatorname{Fil}, Z)$ has Kodaira-Spencer dimension $d$.
7. (Realization.) Every Kodaira-Spencer map $f$ for $(\sigma_0, \varphi, \operatorname{Fil}(A_0), Z(o_0, \beta))$ is realized: there is a deformation of $o_0$ to $k[\varepsilon]$ for which $f x$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$.
8. (Necessity.) For every deformation $o'$ of $o_0$ to $k[\varepsilon]$ there is a Kodaira-Spencer map $g$ for $(\sigma_0, \varphi, \operatorname{Fil}(A_0), Z(o_0, \beta))$ such that $g x$ is a filtration lift of $x$ for $o'$, for every $x \in \operatorname{Fil}(A_0)$.
9. (Lifts are unique up to the filtration.) Let $A'$ be an abelian scheme over $k[\varepsilon]$ with an identification of $A_0$ with its special fibre. Let $x \in \operatorname{Fil}(A_0)$, and let $y$ be a filtration lift of $x$ for $A'$. Then $y'$ is a filtration lift of $x$ for $A'$ if and only if $y' - y \in \operatorname{Fil}(A_0)$.

Results 7, 8 and 9 are the first-order form of the principle that deformations of an abelian variety with its extra structure correspond to lifts of the Hodge filtration that respect this structure. Result 6 is linear algebra: as $r \neq r'$, the space $H$ is the direct sum of the two eigenspaces of $\sigma(w)$.

### Kodaira-Spencer directions

**Theorem 8.21.2 (Kodaira-Spencer directions).** Let $\varphi$ be a polarization pairing of $o_0$. Then $(\sigma_0, \varphi, \operatorname{Fil}(A_0), Z(o_0, \beta))$ has Kodaira-Spencer dimension $a(n - 1)$.

Lean: `GlobalTheory.HTCount.ksDim_at_point` (also `GlobalTheory.T.harrisTaylor_kodairaSpencer_directions_dim`, a second name).

*Proof.* We apply result 6 with $\sigma = \sigma_0$, $s(c) = c^*$, $w$ the image of $\omega$ in $O$, $\operatorname{Fil} = \operatorname{Fil}(A_0)$, $Z = Z(o_0, \beta)$ and the roots $r$ and $r'$. The theorem on [the rho-part count](/entry/rho-count/) gives the Kodaira-Spencer dimension $a(n - 1)$ for $(\sigma_0, 0, \operatorname{Fil}(A_0) + \operatorname{im}(\sigma_0(\omega) - r), Z(o_0, \beta))$. We check the other hypotheses of result 6.

The map $c \mapsto c^*$ is surjective, as $(c^*)^* = c$. Adjointness is result 4. Result 2 gives that $H(A_0)$ is finite-dimensional, that $\varphi$ is skew, and that $\operatorname{Fil}(A_0)$ is isotropic of half dimension. Result 3 gives nondegeneracy, and result 5 stability. The image of $\omega$ lies in the center of $O$, as $O$ is an $\mathcal{O}_F$-algebra, so $\sigma_0(\omega)$ commutes with every $\sigma_0(c)$.

The relations for $\omega$. From $\omega + \bar\omega = t_0$ and $\omega \bar\omega = n_0$ we get $\bar\omega = t_0 - \omega$ and $\omega^2 = t_0 \omega - n_0$. As $r$ is a root of $X^2 - t_0 X + n_0$, we have $r + r' = t_0$ and $r r' = n_0$. So
$$(\sigma_0(\omega) - r)(\sigma_0(\omega) - r') = \sigma_0(\omega)^2 - t_0 \sigma_0(\omega) + n_0 = 0.$$
The involution $*$ restricts to complex conjugation on $\mathcal{O}_F$, so $\omega^* = t_0 - \omega$, and result 4 gives
$$\varphi(\sigma_0(\omega) x, y) = \varphi(x, t_0 y - \sigma_0(\omega) y) = \varphi(x, (r + r') y - \sigma_0(\omega) y).$$

The roots differ. Indeed $(r - r')^2 = t_0^2 - 4n_0$, which is an integer prime to $p$ up to sign. It is a unit in $R$ by Definition 8.1.2, so it is nonzero in $k$.

The Lie subspace lies in the $r'$-part. The space $Z(o_0, \beta)$ is spanned by vectors $\sum_l \lambda_l \sigma_0(c_l) (\sigma_0(\omega) - r') y$. As $\sigma_0(\omega)$ commutes with each $\sigma_0(c_l)$, such a vector equals $(\sigma_0(\omega) - r') \sum_l \lambda_l \sigma_0(c_l) y$. So $Z(o_0, \beta) \subseteq \operatorname{im}(\sigma_0(\omega) - r')$.

Result 6 now gives the theorem. $\square$

### The basis of first-order deformations

**Theorem 8.21.3 (Count of first-order deformations).** Let $d = a(n - 1)$. There are linear maps $f_1, \dots, f_d : H(A_0) \to H(A_0)$ with two properties.

1. For each $j$ there is a deformation of $o_0$ to $k[\varepsilon]$ for which $f_j x$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$.
2. For every deformation $o'$ of $o_0$ to $k[\varepsilon]$ there are unique $c_1, \dots, c_d \in k$ such that $\sum_j c_j f_j x$ is a filtration lift of $x$ for $o'$, for every $x \in \operatorname{Fil}(A_0)$.

Lean: `GlobalTheory.HTCount.count`.

*Proof.* A map of affine schemes $\operatorname{Spec} k \to \operatorname{Spec} R$ comes from a ring map, so $t = \operatorname{Spec} \beta$ for some $\beta$. By result 1, $o_0$ has a polarization pairing $\varphi$. The theorem on Kodaira-Spencer directions gives Kodaira-Spencer maps $f_1, \dots, f_d$ for $(\sigma_0, \varphi, \operatorname{Fil}(A_0), Z(o_0, \beta))$ such that every Kodaira-Spencer map $g$ has unique $c \in k^d$ with $g x - \sum_j c_j f_j x \in \operatorname{Fil}(A_0)$ for all $x \in \operatorname{Fil}(A_0)$.

Property 1 is result 7 applied to each $f_j$.

Property 2. Let $o'$ be a deformation of $o_0$ to $k[\varepsilon]$, with abelian scheme $A'$. Result 8 gives a Kodaira-Spencer map $g$ such that $g x$ is a filtration lift of $x$ for $o'$, for every $x \in \operatorname{Fil}(A_0)$. Take $c$ for $g$ as above. For $x \in \operatorname{Fil}(A_0)$, the difference $\sum_j c_j f_j x - g x$ lies in $\operatorname{Fil}(A_0)$, so by result 9 the vector $\sum_j c_j f_j x$ is a filtration lift of $x$. This gives existence. For uniqueness, let $c'$ be such that $\sum_j c'_j f_j x$ is a filtration lift of $x$ for every $x \in \operatorname{Fil}(A_0)$. Result 9, applied to the lifts $g x$ and $\sum_j c'_j f_j x$, gives $g x - \sum_j c'_j f_j x \in \operatorname{Fil}(A_0)$. By the uniqueness of $c$, we get $c' = c$. $\square$

**Remark 8.21.4 (Formalization).** The count is in [HarrisTaylorFirstOrderDeformationsBasisCount.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorFirstOrderDeformationsBasisCount.lean#L17), and the theorem on Kodaira-Spencer directions in [HarrisTaylorKodairaSpencerDirectionsDim.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorKodairaSpencerDirectionsDim.lean#L27). Its second name is a wrapper that tries three forms of one proof term under a raised heartbeat limit: [HarrisTaylorKodairaSpencerDirectionsDimStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorKodairaSpencerDirectionsDimStatement.lean#L7). The computation that $r \neq r'$ is done twice, here and in the rho-part count. The Chern class condition in a polarization pairing is a predicate that we have not unfolded; the words "de Rham Chern class" are our reading of it. Result 6 is stated for a space $H$ in the universe `Type 1`. We read the statements of results 1 to 9, not their proofs. In result 9 the identification of $A_0$ with the special fibre is a group pullback square along $\operatorname{Spec} k \to \operatorname{Spec} k[\varepsilon]$.
