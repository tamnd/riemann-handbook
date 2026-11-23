---
title: Periods in families and the Gauss-Manin connection
decls:
  - GlobalTheory.AnPer.gaussManinPeriods_of_span_taylor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Periods in families and the Gauss-Manin connection

This section reduces the Gauss-Manin periods statement to two of its parts, a span statement and a Taylor statement (Theorem (Gauss-Manin periods from span and Taylor)). The statement says that the period maps of the fibres of an abelian scheme over a smooth $\mathbb{C}$-algebra can be chosen to vary holomorphically, compatibly with endomorphisms, and so that their Taylor expansions compute the transport of de Rham homology over nilpotent divided power thickenings. It is used on the way to [EveryCharacter](/step/every-character/).

We keep the notation of the last section: holomorphic uniformizations $u = (e, \Lambda, \theta)$, periods, and period maps of sign $\varepsilon$.

A *family of lattices* over an open set $V \subset \mathbb{C}^I$, for a finite set $I$, is an abelian group $\Lambda$ with an additive map $\tau$ from $\Lambda$ to the holomorphic maps $V \to \mathbb{C}^g$. Let $X$ be a scheme over a ring $B$ and $\sigma : B \to \mathcal{O}(V)$ a ring map into the holomorphic functions on $V$. A *uniformization* of $X$ over $\sigma$ is a map $E$ from $\mathbb{C}^I \times \mathbb{C}^g$ to the $\mathbb{C}$-points of $X$ such that, for $z \in V$, $E(z, w)$ lies over the point $b \mapsto \sigma(b)(z)$ of $B$ and $E(z, w + \tau(l)(z)) = E(z, w)$, and such that regular functions of $X$ pull back to holomorphic functions on open sets, as in condition 2 above. It is *based* if the points $E(z, 0)$, $z \in V$, lie in one affine open set. A *period* of a class $c \in H^1_{\mathrm{dR}}(X / B)$ for $E$ is an additive map $\mathrm{per}$ from $\Lambda$ to the holomorphic functions on $V$ such that the pullback of $c$ to every system of analytic charts compatible with $E$ is the class defined by $\mathrm{per}$. A holomorphic uniformization of an abelian scheme $A$ over $\mathbb{C}$ is a uniformization over a point, and an additive $P : \Lambda \to D_{\mathrm{dR}}(A)$ is a *period homomorphism* if for every primitive $c$ the constants $P(l)(c)$ form a period of $c$ in this sense.

For an ideal with nilpotent divided powers $\kappa$ and a surjection $\pi : D \to \mathbb{C}$ with kernel that ideal, let $D_\kappa(A_0)$ be the crystalline de Rham homology of $A_0$ relative to $(D, \ker \pi, \kappa)$, as in the section on lifting along nilpotent divided powers. For $t \in D^I$ with $\pi(t_i) = 0$ and $f$ holomorphic near $0$, write
$$T_N(f)(t) = \sum_{k = 0}^{N} \frac{1}{k!} \sum_{s : \{1, \dots, k\} \to I} \partial_{s_1} \cdots \partial_{s_k} f(0)\, t_{s_1} \cdots t_{s_k}$$
for the Taylor polynomial of order $N$ evaluated at $t$.

The *span statement* says: for every abelian scheme $A$ over $\mathbb{C}$, smooth of relative dimension $g$, every line bundle $L$, every holomorphic uniformization of $(A, L)$ of dimension $g$ and every period homomorphism $P$, condition 1 holds.

The *Taylor statement* concerns an abelian scheme $\mathcal{A}$ over a $\mathbb{C}$-algebra $B$, smooth of relative dimension $g$, a fibre $A_0$ of $\mathcal{A}$ at a point $y_0$ of $B$, a holomorphic uniformization $u_0$ of $A_0$ with lattice $\Lambda_0$, and a uniformization $E$ of $\mathcal{A}$ over some $\sigma$, on a family of lattices on $\Lambda_0$ over $V \ni 0$, that restricts at $0$ to $y_0$, to $u_0$ and to the identity of $\Lambda_0$. Let $P_0$ be a period homomorphism of $u_0$. Let $D$, $\kappa$ and $\pi$ be as above, $t \in D^I$ with $\pi(t_i) = 0$ and all products of $N + 1$ of the $t_i$ zero, $j : B \to D$ the $\mathbb{C}$-algebra map $b \mapsto T_N(\sigma(b))(t)$, $A'$ the base change of $\mathcal{A}$ along $j$, with $A_0 \to A'$ over $\pi$. The statement says: for $x \in \Lambda_0$, $d \in D_\kappa(A_0)$ that corresponds to $P_0(x)$, $c$ primitive on $\mathcal{A}$ and $\mathrm{per}$ a period of $c$ for $E$, the image of $d$ in $D_{\mathrm{dR}}(A')$, evaluated at the pullback of $c$, is $T_N(\mathrm{per}(x))(t)$.

The map $D_\kappa(A_0) \to D_{\mathrm{dR}}(A')$ is the dual of the rigidity isomorphism of the section on the de Rham structure.

**Theorem 1.22.1 (Gauss-Manin periods from span and Taylor).** Assume the span statement and the Taylor statement. Then there is $\varepsilon = \pm 1$ with the following property. Let $B$ be a smooth $\mathbb{C}$-algebra, $\mathcal{A}$ an abelian scheme over $B$, smooth of relative dimension $g$, $U \subset \mathbb{C}^I$ an open neighbourhood of $0$, and $y_z$, for $z \in \mathbb{C}^I$, points of $B$ such that $z \mapsto y_z(b)$ is holomorphic on $U$ for each $b$. Let $A_z$ be the fibre of $\mathcal{A}$ at $y_z$, as a group, $m_z$ the induced map on de Rham cohomology, and $L_z$ any line bundle on $A_z$. Let $A_0'$ be the fibre at $y_0$, $L_0'$ a line bundle on it and $u_0'$ a holomorphic uniformization of $(A_0', L_0')$ of dimension $g$, with map $e_0'$ and lattice $\Lambda_0$. Then there are an open set $V$ with $0 \in V \subset U$, holomorphic uniformizations $u_z$ of $(A_z, L_z)$ of dimension $g$, isomorphisms $\tau_z : \Lambda_0 \to \Lambda_z$, and additive maps $P_z : \Lambda_z \to D_{\mathrm{dR}}(A_z)$ and $P_0' : \Lambda_0 \to D_{\mathrm{dR}}(A_0')$, such that:

1. $P_0'$ and each $P_z$ with $z \in V$ are period maps of sign $\varepsilon$;
2. $e_0(w)$ and $e_0'(w)$ have the same image in $\mathcal{A}$ for all $w$, where $e_z$ is the map of $u_z$; $\tau_0(x) = x$; and $z \mapsto \tau_z(x)$ is holomorphic on $V$;
3. if an endomorphism $\alpha$ of $\mathcal{A}$ as a group and a linear map $M_0$ satisfy $\alpha(e_0'(w)) = e_0'(M_0 w)$ in $\mathcal{A}$, then for each $z \in V$ there is a linear $M$ with $\alpha(e_z(w)) = e_z(M w)$ in $\mathcal{A}$ and $\tau_z(M_0 x) = M \tau_z(x)$;
4. for $x \in \Lambda_0$ and $c$ primitive on $\mathcal{A}$, $z \mapsto P_z(\tau_z x)(m_z^* c)$ is holomorphic on $V$;
5. in the setting of the Taylor statement, for $j(b) = T_N(z \mapsto y_z(b))(t)$, $x \in \Lambda_0$, $d$ corresponding to $P_0'(x)$ and $c$ primitive, the image of $d$ evaluated at the pullback of $c$ is $T_N(z \mapsto P_z(\tau_z x)(m_z^* c))(t)$.

Lean: `GlobalTheory.AnPer.gaussManinPeriods_of_span_taylor`.

The line bundles $L_z$ are arbitrary. Clause 5 says that the periods move by the Gauss-Manin connection: their Taylor expansion at $0$ computes the crystalline transport of $P_0'(x)$.

We use seven facts besides the two hypotheses.

1. (Families of uniformizations.) For $B$ of finite type and data as in the theorem, there are $r > 0$ with the ball $V_r$ of radius $r$ in $U$, uniformizations $u_z$ and isomorphisms $\tau_z$, such that $(z, w) \mapsto e_z(w)$ is holomorphic into $\mathcal{A}$ on $V_r \times \mathbb{C}^g$, the points $e_z(0)$ for $z \in V_r$ lie in one affine open set, and clauses 2 and 3 hold on $V_r$.
2. (Existence.) For a based uniformization, every class has a period.
3. (Period homomorphisms.) Every holomorphic uniformization of an abelian scheme over $\mathbb{C}$ has a period homomorphism.
4. (Lie.) Period homomorphisms satisfy condition 2 of a period map, if $A$ is smooth of relative dimension $g$.
5. (Endomorphisms.) Period homomorphisms satisfy condition 3.
6. (Riemann forms.) Period homomorphisms satisfy condition 4 with $\varepsilon = -1$.
7. (Fibres.) Let $E$ be a uniformization of $\mathcal{A}$ over $\sigma$, $z \in V$, $A$ the fibre at $b \mapsto \sigma(b)(z)$ with a uniformization $u$ matching $E(z, \cdot)$ and $\tau$ matching $\tau(\cdot)(z)$, $P$ a period homomorphism of $u$, $c$ primitive on $\mathcal{A}$ and $\mathrm{per}$ a period of $c$ for $E$. Then $P(\tau l)(m^* c) = \mathrm{per}(l)(z)$.

*Proof.* Take $\varepsilon = -1$. Let $A$ be an abelian scheme over $\mathbb{C}$, smooth of relative dimension $g$, and $P$ a period homomorphism of a uniformization of $(A, L)$. The span statement gives condition 1 of a period map, and facts 4 to 6 give conditions 2 to 4, so $P$ is a period map of sign $-1$.

Now let the data be as in the theorem. A smooth algebra is of finite type, so fact 1 gives $r$, $u_z$ and $\tau_z$; let $V = V_r$. The fibres $A_z$ and $A_0'$ are abelian schemes, smooth of relative dimension $g$, as base changes of $\mathcal{A}$. Fact 3 gives period homomorphisms $P_z$ of $u_z$ and $P_0'$ of $u_0'$, which are period maps of sign $-1$ by the first paragraph. This is clause 1, and fact 1 gives clauses 2 and 3.

The $\tau_z$ form a family of lattices on $\Lambda_0$ over $V$, and $\sigma(b)(z) = y_z(b)$ defines $\sigma : B \to \mathcal{O}(V)$. The maps $E(z, w) = e_z(w)$, composed into $\mathcal{A}$, form a uniformization of $\mathcal{A}$ over $\sigma$, which is based by fact 1. Fact 2 gives a period $\mathrm{per}_c$ of each primitive $c$, and fact 7 gives $P_z(\tau_z x)(m_z^* c) = \mathrm{per}_c(x)(z)$ for $z \in V$. Since $\mathrm{per}_c(x)$ is holomorphic, this gives clause 4. For clause 5, the Taylor polynomial depends only on the germ at $0$, so $j(b) = T_N(\sigma(b))(t)$. The Taylor statement for $E$ gives the value $T_N(\mathrm{per}_c(x))(t)$, which equals $T_N(z \mapsto P_z(\tau_z x)(m_z^* c))(t)$ by the identity above. $\square$

**Remark 1.22.2 (Formalization).** The theorem proves `GlobalTheory.Published.GaussManinPeriods` ([GaussManinPeriods.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/GaussManinPeriods.lean#L37)) from the hypotheses `PSpan` and `PTaylor` ([IsPeriodHom.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsPeriodHom.lean#L93)), by `GlobalTheory.AnPer.gaussManinPeriods_of_parts` with $\varepsilon = -1$. Facts 1 to 7 are `GlobalTheory.PeriodFamily.famUnif_holds`, `GlobalTheory.T.periods_exist_affine_zero_section`, `GlobalTheory.T.exists_integrationOverCyclesHom`, `GlobalTheory.T.integrationOverCycles_lifts_lieLattice`, `GlobalTheory.T.periodHom_push_end'`, `GlobalTheory.T.pChern_neg_one` and `GlobalTheory.T.fibrePeriod_eq_familyPeriod_value`, cited by their statements. The two hypotheses are discharged elsewhere: `GlobalTheory.PeriodFamily.gaussManinPeriods_holds` ([GaussManinPeriodsHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GaussManinPeriodsHolds.lean#L12)) proves `PSpan` from Theorem (Periods span de Rham homology) of the last section and `GlobalTheory.PerLink.main`, which turns a period in the family sense into a period of $\gamma(c)$, and takes `GlobalTheory.AnPer.TaylorClause.pTaylor0` for `PTaylor`. The family periods `IsPeriod` and the class `perCl` of a period on the analytic charts were not unfolded, and the description of them above is a reading of their names and types. Condition 4 of a period map (`GlobalTheory.PeriodFamily.IsPeriodMap`, in the same file as the statement) is stated only for $L$ and the frames of $u$, although fact 6 allows any line bundle with the same $e$. The statement asks for $\varepsilon$, and the proof fixes $\varepsilon = -1$.


## Notes and references

The chapter feeds [EveryCharacter](/step/every-character/) and [EveryCharacter from Row0b](/step/every-character-of-row/). The [dual abelian scheme](/entry/dual-abelian-scheme/) is the statement on duals in [the CM and abelian variety inputs](/step/cm-abelian-inputs-from-literature/). The [lifting of homomorphisms along nilpotent divided powers](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/), the [Hodge and de Rham structure](/entry/ab-coh-abelian-hodge-de-rham/), [unobstructedness](/entry/abelian-unobstructed/), the [ample roots](/entry/exists-ample-root/), the [algebraization of morphisms](/entry/formal-algebraisation-morphisms/) and the [Gauss-Manin periods](/entry/gauss-manin-periods-of-span-taylor/) enter at EveryCharacter.

**Remark 1.23.1 (The dual over a general base).** The statement proved in the section on the dual over any base assumes only that $S$ is a scheme and that $A$ is an abelian scheme over $S$: a commutative group scheme that is smooth and proper with geometrically connected fibres. It assumes no projectivity, no polarization and no noetherian condition. It asserts a dual $B$ that is a scheme. The general results in the literature give the dual of an abelian scheme as an algebraic space, and as a scheme under extra hypotheses, for example for projective $A$ (Faltings and Chai, Chapter I, §1); Raynaud gives abelian schemes that are not projective over their base. So the Lean statement does not assume more than the literature; it claims more. The proof in this chapter builds $B$ through a limit argument, noetherian induction, pinching from normal domains and relatively ample bundles there, and Zariski gluing. We have not located the step at which it goes beyond the published results, and the statement should be audited against the sources below.

D. Mumford, *Abelian Varieties*, Chapter I, §1 and §2, for complex tori, their cohomology $\mathrm{Hom}(\Lambda, \mathbb{C})$ and the Appell-Humbert theorem, used in the last two sections.

D. Mumford, *Abelian Varieties*, Chapter II, §5 and §6, for cohomology and base change and the theorem of the cube.

D. Mumford, *Abelian Varieties*, Chapter III, §13, for the dual abelian variety over a field and the cohomology of the structure sheaf.

D. Mumford, J. Fogarty and F. Kirwan, *Geometric Invariant Theory*, third edition, Chapter 6, for rigidity, the dual of a projective abelian scheme and deformations of abelian schemes.

G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Chapter I, §1, for the dual of an abelian scheme as an algebraic space and as a scheme in the projective case.

M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Lecture Notes in Math. 119, Chapitre XI, for the projectivity of abelian schemes over a normal base, the source of the theorem on ample bundles over normal domains.

A. Grothendieck, *Éléments de géométrie algébrique III*, Publ. Math. IHÉS 11, Théorème 5.1.4 and Théorème 5.4.1, for the existence theorem for coherent sheaves and for morphisms.

A. Grothendieck, *Éléments de géométrie algébrique IV*, Part 4, Publ. Math. IHÉS 32, §17, for smooth morphisms and the lifting of sections along nilpotent thickenings.

M. Demazure and A. Grothendieck, *Schémas en groupes I* (SGA 3), Lecture Notes in Math. 151, Exposé II for tangent spaces of group schemes and Exposé VI_B for the identity component of a smooth group scheme.

F. Oort, "Finite group schemes, local moduli for abelian varieties, and lifting problems", Compositio Math. 23 (1971), §2, for the unobstructedness of deformations of abelian schemes.

W. Messing, *The Crystals Associated to Barsotti-Tate Groups: with Applications to Abelian Schemes*, Lecture Notes in Math. 264, Chapter V, for the deformation theory of abelian schemes along nilpotent divided powers.

B. Mazur and W. Messing, *Universal Extensions and One Dimensional Crystalline Cohomology*, Lecture Notes in Math. 370, Chapter II, for the crystalline nature of the first de Rham cohomology of an abelian scheme and the lifting of homomorphisms.

The treatment here differs from these sources in three ways. Cohomology is computed on the category of affine opens and on the infinitesimal site, through ordered Čech complexes, rather than by derived functors. The dual is built through noetherian induction and pinching rather than by the Picard functor. Over $\mathbb{C}$, periods are defined by holomorphic primitives on $\mathbb{C}^g$, and the Gauss-Manin connection enters only through Taylor expansions over nilpotent divided power thickenings.
