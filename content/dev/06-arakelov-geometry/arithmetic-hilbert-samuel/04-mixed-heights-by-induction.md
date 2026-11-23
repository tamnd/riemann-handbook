---
title: Mixed heights by induction on the dimension
decls:
  - GlobalTheory.MixHt.Step.isMix_succ
  - GlobalTheory.T.isMixedHeightByInduction_succ
  - GlobalTheory.MixHt.exists_isMix_of_arch
  - GlobalTheory.T.exists_mixedHeight_of_archimedean_integrals
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mixed heights by induction on the dimension

The [[height|F1FF505PWH]] of an integral subvariety $Z$ of an arithmetic variety with respect to hermitian line bundles $\bar L_1, \dots, \bar L_d$, with $d = \dim Z$, is the arithmetic intersection number $\widehat{\deg}(\hat c_1(\bar L_1) \cdots \hat c_1(\bar L_d) \mid Z)$. Bost, Gillet and Soulé compute it by induction on $d$: cut $Z$ by the divisor of a rational section of $\bar L_1$ and add an archimedean integral. This section turns the induction into a construction. Given two analytic statements, the integrability of the archimedean integrals and [the archimedean reciprocity law](/entry/arch-recip-of-principalisation/), we build for every $m$ a system of mixed heights in dimensions up to $m$. The system feeds [the arithmetic intersection calculus](/entry/ar-form-exists-ar-mix-height-projection/).

### The axioms

**Definition 6.4.1 (Ambient scheme).** An ambient scheme is a scheme $X$ with a morphism $p : X \to \operatorname{Spec} k$, where $k$ is a domain finite as a $\mathbb{Z}$-module and $X$ is projective over $k$.

Every arithmetic variety and every integral closed subscheme of an ambient scheme is ambient. A point $x$ of $X$ has dimension $d$ if its closure has dimension $d$; we write $\overline{\{x\}}$ for the closure, with its reduced structure, and $\kappa(x)$ for the residue field.

For a hermitian line bundle $\bar M$ on an integral scheme $Y$ of dimension $e + 1$, a rational section $r$ and a family $\bar{\mathbf L} = (\bar L_1, \dots, \bar L_e)$, the archimedean term is
$$I_\infty(\bar{\mathbf L}; \bar M, r) = \sum_\sigma \int_{Y_\sigma(\mathbb{C})} \log\|r\|_\sigma \, c_1(\bar L_1) \cdots c_1(\bar L_e),$$
the polarised integral of $\log\|r\|$ over the complement of the support of $\operatorname{div} r$. We put
$$\operatorname{rec}(h; \bar{\mathbf L}; \bar M, r) = \sum_z \operatorname{mult}_z(\operatorname{div} r) \, h(z) - I_\infty(\bar{\mathbf L}; \bar M, r)$$
for a function $h$ on the points of codimension one.

**Definition 6.4.2 (Mixed heights up to dimension $m$).** Let $X$ be ambient. A system of mixed heights up to dimension $m$ assigns to each $d$, each family $\bar{\mathbf L} = (\bar L_1, \dots, \bar L_d)$ of hermitian line bundles on $X$ and each point $x$ a real number $T_d(\bar{\mathbf L})(x)$, with five properties.
1. Isometry: if $d \le m$, $x$ has dimension $d$ and $\bar L_a$ is isometric to $\bar M_a$ for all $a$, then $T_d(\bar{\mathbf L})(x) = T_d(\bar{\mathbf M})(x)$.
2. Symmetry: if $d \le m$ and $x$ has dimension $d$, then $T_d(\bar{\mathbf L})(x)$ is invariant under permutations of the family.
3. Additivity: if $d + 1 \le m$ and $x$ has dimension $d + 1$, then $T_{d+1}(\bar A \otimes \bar B, \bar{\mathbf L})(x) = T_{d+1}(\bar A, \bar{\mathbf L})(x) + T_{d+1}(\bar B, \bar{\mathbf L})(x)$.
4. Points: if $x$ has dimension $0$, then $T_0(x) = \log \# \kappa(x)$.
5. Recursion: let $i : Y \to X$ be an integral closed subscheme of dimension $e + 1 \le m$, let $\bar M$ and $\bar{\mathbf L} = (\bar L_1, \dots, \bar L_e)$ be bundles on $X$ whose restrictions are isometric to $\bar M'$ and $\bar{\mathbf L}'$ on $Y$, and let $r$ be a rational section of $M'$. Then
$$T_{e+1}(\bar M, \bar{\mathbf L})(\eta_Y) = \operatorname{rec}\big(z \mapsto T_e(\bar{\mathbf L})(i(z)); \bar{\mathbf L}'; \bar M', r\big),$$
where $\eta_Y$ is the generic point of $Y$.

The recursion is the inductive formula of Bost, Gillet and Soulé for heights of cycles. The value $T_d(\bar{\mathbf L})(x)$ is the mixed height of the closure of $x$. The constant function $T_d = \log \#\kappa(x)$ is a system up to dimension $0$: properties 1 and 2 hold trivially, 4 holds by definition, and 3 and 5 are empty.

**Definition 6.4.3 (Archimedean integrability).** We say that archimedean integrability holds if for every arithmetic variety $Y$ of relative dimension $e$, all hermitian line bundles $\bar M$, $\bar N$ and every rational section $r$ of $M$, the function $\log\|r\|_\sigma$ is integrable for $c_1(\bar N)^e$ on the complement of the support of $\operatorname{div} r$, at every $\sigma$.

### The inductive step

**Theorem 6.4.4 (Mixed heights, inductive step).** Assume archimedean integrability and archimedean reciprocity. Let $m \ge 0$, and assume that every ambient scheme has a system of mixed heights up to dimension $m$. Then every ambient scheme has a system of mixed heights up to dimension $m + 1$.

Lean: `GlobalTheory.MixHt.Step.isMix_succ` (also `GlobalTheory.T.isMixedHeightByInduction_succ`, a second name).

*Proof.* Let $X$ be ambient with a system $T$ up to dimension $m$. We keep $T_d$ for all $d \ne m + 1$ and at points of dimension other than $m + 1$, and we define a new value at points $x$ of dimension $m + 1$.

Definition of the new value. Let $x$ have dimension $m + 1$, with closure $Y$, and let $\bar M, \bar L_1, \dots, \bar L_m$ be bundles on $X$. Choose a rational section $r$ of $\bar M|_Y$ and put
$$V(\bar M, \bar{\mathbf L})(x) = \operatorname{rec}\big(z \mapsto T_m(\bar{\mathbf L})(z); \bar{\mathbf L}|_Y; \bar M|_Y, r\big).$$
This number does not depend on the choice of $r$. Two sections differ by a rational function $f$; the divisor term changes by $\sum_z \operatorname{ord}_z(f) T_m(\bar{\mathbf L})(z)$ and the archimedean term by $\sum_\sigma \int \log|f| \, c_1(\bar{\mathbf L})$, and the two changes must cancel. This cancellation is a result of the development, proved from the two analytic statements and the systems up to dimension $m$; we take it as given. The value also does not depend on the choice of a system on $Y$: two systems up to dimension $m$ agree on the restrictions of bundles to closed subschemes, by uniqueness of mixed heights, and the recursion for a system on $Y$ computes the same number.

Isometry and recursion in dimension $m + 1$ hold by construction, since $V$ is the right side of the recursion and the archimedean term only depends on the isometry classes. Points of dimension $0$ are unchanged, so property 4 holds.

Additivity. Let $r$ and $r'$ be rational sections of $\bar A|_Y$ and $\bar B|_Y$. Then $r \otimes r'$ is a rational section of $(\bar A \otimes \bar B)|_Y$, with $\operatorname{div}(r \otimes r') = \operatorname{div} r + \operatorname{div} r'$ and $\log\|r \otimes r'\| = \log\|r\| + \log\|r'\|$. Both terms of the recursion are additive, so $V$ is additive in the first bundle.

Symmetry. For $m = 0$ there is one bundle and nothing to prove. For $m \ge 1$ it is enough to prove invariance under permutations of the last $m$ bundles and under the exchange of the first two, since these generate the symmetric group. The last $m$ bundles enter $V$ through $T_m(\bar{\mathbf L})$, which is symmetric by hypothesis, and through the archimedean term, which is a polarised integral and so symmetric. The exchange of the first two bundles $\bar M$ and $\bar N$ is a cited result of the development, and it is the step that uses reciprocity. In outline: choose sections $s$ of $\bar M|_Y$ and $t$ of $\bar N|_Y$ with no common divisor. Expand $T_m(\bar N, \dots)$ at the points of $\operatorname{div} s$ by the recursion with $t$, and $T_m(\bar M, \dots)$ at the points of $\operatorname{div} t$ by the recursion with $s$. The two double sums over points of dimension $m - 1$ agree, since both count the intersection of $\operatorname{div} s$ and $\operatorname{div} t$. The remaining archimedean terms are the two sides of [the archimedean reciprocity law](/entry/arch-recip-of-principalisation/), so they agree too. $\square$

**Theorem 6.4.5 (Existence of mixed heights).** Assume archimedean integrability and archimedean reciprocity. Then every ambient scheme has, for every $m$, a system of mixed heights up to dimension $m$.

Lean: `GlobalTheory.MixHt.exists_isMix_of_arch` (also `GlobalTheory.T.exists_mixedHeight_of_archimedean_integrals`, a second name).

*Proof.* By induction on $m$. For $m = 0$ take $T_d(x) = \log\#\kappa(x)$. The step is [the inductive step](/entry/is-mix-succ/). $\square$

**Remark 6.4.6 (Formalization).** The induction runs over all ambient schemes at once, since the recursion on $X$ needs systems on closed subschemes. In the point axiom, $\#\kappa(x)$ is a cardinal that is set to $0$ for an infinite field; it is only used at closed points, whose residue fields are finite. The new value at points of dimension $m + 1$ is defined by a choice of the well defined value, and the symmetry is reduced to transpositions of the first two bundles and permutations of the tail by a lemma on generators of the symmetric group. The file of the existence theorem ends with an `example` that restates it ([ExistsMixedHeightOfArchimedeanIntegrals.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsMixedHeightOfArchimedeanIntegrals.lean#L24)).
