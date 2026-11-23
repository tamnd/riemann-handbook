---
title: Tangent vectors and sections over thickenings
decls:
  - GlobalTheory.T.exists_tangentRepresentation_smooth_groupScheme
  - GlobalTheory.TanRepr.exists_tanRep
  - GlobalTheory.TanRepr.tanRep
  - GlobalTheory.SecLift.exists_section_lift
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Tangent vectors and sections over thickenings

This section proves two results on [[smooth|EXKGG9X6J0]] schemes over a thickening of the base. The first describes first order deformations of the unit section of a smooth group scheme $A$ over a ring $R$ (Theorem (Tangent representation)). For an $R$-algebra $B$ and a $B$-module $M$, the points of $A$ with values in the square zero extension $B \oplus M$ that lift the unit are the $R$-linear maps $W \to M$, for one finite projective $R$-module $W$, naturally in $(B, M)$. The module $W$ is the module of invariant differentials, and its dual is the Lie algebra. The second result lifts sections of a smooth scheme along a nilpotent thickening of an affine base (Theorem (Lifting sections)). Both are used on the way to [EveryCharacter](/step/every-character/): the first to identify Lie algebras and tangent spaces, the second to lift points, such as the unit or torsion points, from $R_0$ to $R$.

Throughout, $R$ is a ring. For an $R$-algebra $B$ and a $B$-module $M$, let $B \oplus M$ be the *square zero extension*: the ring with $(b, m)(b', m') = (bb', bm' + b'm)$. It is a $B$-algebra, and $(b, m) \mapsto b$ is a surjection onto $B$ whose kernel $M$ has square zero. For $M = B$ we get the dual numbers $B[\varepsilon]$. A ring map $\beta : B \oplus M \to B' \oplus M'$ is *of sum form* if there are maps $\alpha : B \to B'$ of $R$-algebras and $f : M \to M'$ of $R$-modules with $\beta(b, 0) = (\alpha(b), 0)$ and $\beta(0, m) = (0, f(m))$.

Let $A$ be a group scheme over $\mathrm{Spec}\, R$ with unit section $e$. For an $R$-algebra $B$, the *unit point* $e_B \in A(B)$ is the composite $\mathrm{Spec}\, B \to \mathrm{Spec}\, R \xrightarrow{e} A$. A morphism $z : \mathrm{Spec}(B \oplus M) \to A$ *lifts the unit* if $z$ is a morphism over $R$, where $\mathrm{Spec}(B \oplus M)$ lies over $R$ through $R \to B \to B \oplus M$, and the restriction of $z$ to $\mathrm{Spec}\, B$, along $B \oplus M \to B$, is $e_B$.

**Definition 1.17.1 (Tangent representation).** Let $A$ be a group scheme over $\mathrm{Spec}\, R$ and $W$ an $R$-module. A *tangent representation of $A$ on $W$* is a rule $\Phi$ that assigns to each $R$-algebra $B$, each $B$-module $M$ and each morphism $z : \mathrm{Spec}(B \oplus M) \to A$ an $R$-linear map $\Phi(z) : W \to M$, such that:

1. (Bijectivity.) For each $R$-linear map $l : W \to M$, there is exactly one $z$ that lifts the unit and has $\Phi(z) = l$.
2. (Naturality.) For each ring map $\beta : B \oplus M \to B' \oplus M'$ of sum form $(\alpha, f)$ and each $z$ that lifts the unit, $\Phi(z \circ \mathrm{Spec}\, \beta) = f \circ \Phi(z)$.

So the set of lifts of the unit to $B \oplus M$ is $\mathrm{Hom}_R(W, M)$, naturally in $B$ and $M$. If $W$ is finite projective, then $\mathrm{Hom}_R(W, M) = W^\vee \otimes_R M$, and with $B = R$ and $M = R$ the tangent vectors of $A$ at the unit, that is the points over $R[\varepsilon]$ that reduce to $e$, form $W^\vee = \mathrm{Lie}(A)$. This is the functorial form of the statement that the tangent space at the unit is the dual of the cotangent space $e^* \Omega_{A/R}$.

**Definition 1.17.2 (Cotangent module).** Let $A$ be a group scheme over $\mathrm{Spec}\, R$ with unit section $e$. Let $\omega_A$ be the conormal sheaf of $e$, a sheaf of modules on $\mathrm{Spec}\, R$, and $W_A = \Gamma(\mathrm{Spec}\, R, \omega_A)$ its module of global sections. For a morphism $v : \mathrm{Spec}(R \oplus M) \to A$ over $R$ that restricts to $e$ on $\mathrm{Spec}\, R$, let $\Phi_v : W_A \to M$ be the map that evaluates a cotangent form at $v$: a section of $\omega_A$ is the class of a function $a$ vanishing along $e$, and $\Phi_v$ sends it to the $M$ part of $v^* a$.

When $\omega_A$ is quasicoherent, $W_A$ determines $\omega_A$, and the evaluation maps are the tangent representation.

**Proposition 1.17.3 (Tangent representation on the cotangent module).** Let $A$ be a group scheme over $\mathrm{Spec}\, R$ whose sheaf $\omega_A$ is quasicoherent. For $z : \mathrm{Spec}(B \oplus M) \to A$, put $\Phi(z) = \Phi_v$ if $z$ is the composite of $\mathrm{Spec}(B \oplus M) \to \mathrm{Spec}(R \oplus M)$ with some $v : \mathrm{Spec}(R \oplus M) \to A$ that restricts to $e$, and $\Phi(z) = 0$ otherwise. Then $\Phi$ is a tangent representation of $A$ on $W_A$.

Lean: `GlobalTheory.TanRepr.tanRep`.

In the definition, $\mathrm{Spec}(B \oplus M) \to \mathrm{Spec}(R \oplus M)$ comes from the ring map $R \oplus M \to B \oplus M$, $(r, m) \mapsto (r, m)$. The value $0$ in the second case is a convention; it does not enter the two conditions when $z$ lifts the unit, since such a $z$ factors through some $v$ (this is the first step of the proof).

*Proof.* Let $z$ lift the unit. Because $z$ is a morphism over $R$ and restricts to the unit, it factors through a first order neighbourhood of $e$, and so through some $v : \mathrm{Spec}(R \oplus M) \to A$ that restricts to $e$; any two such $v$ give the same $z$ and the same $\Phi_v$. Since $\omega_A$ is quasicoherent and $M$ has square zero, the morphisms $v$ that restrict to $e$ correspond to $R$-linear maps $W_A \to M$, by $v \mapsto \Phi_v$. This gives bijectivity. Naturality holds because $\Phi_v$ is the $M$ part of a pullback of functions, and a map of sum form acts on the $M$ part by $f$. $\square$

**Theorem 1.17.4 (Tangent representation).** Let $A$ be a group scheme over $\mathrm{Spec}\, R$ with $A \to \mathrm{Spec}\, R$ smooth. Then there are a finite projective $R$-module $W$ and a tangent representation of $A$ on $W$.

Lean: `GlobalTheory.TanRepr.exists_tanRep` (also `GlobalTheory.T.exists_tangentRepresentation_smooth_groupScheme`, a second name).

*Proof.* Since $A$ is smooth, $\Omega_{A/R}$ is locally free of finite rank, and $\omega_A = e^* \Omega_{A/R}$. Locally on $\mathrm{Spec}\, R$ it has a frame: a finite basis of cotangent forms. A sheaf of modules with such local frames is quasicoherent, and its global sections $W_A$ are a finite projective $R$-module. The Proposition (Tangent representation on the cotangent module) gives a tangent representation on $W = W_A$. $\square$

The second result is about sections. For a ring map $\pi : R \to R_0$, a scheme $X$ over $R$ and a cartesian square
$$\begin{array}{ccc} X_0 & \xrightarrow{\ i\ } & X \\ \downarrow & & \downarrow \\ \mathrm{Spec}\, R_0 & \xrightarrow{\ \mathrm{Spec}\, \pi\ } & \mathrm{Spec}\, R, \end{array}$$
a section $e$ of $X \to \mathrm{Spec}\, R$ *lifts* a section $e_0$ of $X_0 \to \mathrm{Spec}\, R_0$ if $i \circ e_0 = e \circ \mathrm{Spec}\, \pi$.

**Theorem 1.17.5 (Lifting sections).** Let $\pi : R \to R_0$ be a surjective ring map whose kernel is a nilpotent ideal. Let $X$ be a smooth scheme over $R$, $X_0 \to X$ its base change along $\mathrm{Spec}\, \pi$, and $e_0$ a section of $X_0 \to \mathrm{Spec}\, R_0$. Then there is a section $e$ of $X \to \mathrm{Spec}\, R$ that lifts $e_0$.

Lean: `GlobalTheory.SecLift.exists_section_lift`.

This is the infinitesimal lifting property of smooth morphisms, for a section over an affine base. Locally it is the definition of formal smoothness. The point is the passage from local to global lifts.

*Proof.* Let $I$ be the kernel of $\pi$, with $I^n = 0$. The quotients $R / I^{k}$ give a chain of surjections $R = R/I^n \to R/I^{n-1} \to \dots \to R/I = R_0$, each with a kernel of square zero, and a smooth scheme stays smooth under base change. So by induction on $n$ it suffices to treat the case $I^2 = 0$. Assume this, and let $g_0 = i \circ e_0 : \mathrm{Spec}\, R_0 \to X$, a morphism over $\mathrm{Spec}\, \pi$.

Local lifts. Let $J$ be the set of $h \in R$ for which there are an affine open $V \subset X$ and a morphism $e_h : \mathrm{Spec}\, R_h \to V$ over $R$ that restricts to $g_0$ over $\mathrm{Spec}\, (R_0)_{\pi(h)}$. For each prime $\mathfrak{p}$ of $R$ there is $h \in J$ with $h \notin \mathfrak{p}$: take an affine open $V$ of $X$ that contains the image under $g_0$ of the point $\mathfrak{p}$, then $h$ with $g_0(D(\pi(h))) \subset V$ and $h \notin \mathfrak{p}$, and lift the map of affine schemes $\mathrm{Spec}\, (R_0)_{\pi(h)} \to V$ to $\mathrm{Spec}\, R_h$, which is possible since $V$ is smooth and affine over $R$ and $I_h$ has square zero. So no maximal ideal contains $J$, the ideal generated by $J$ is $R$, and there are finitely many $h_1, \dots, h_n \in J$ that generate the unit ideal.

Gluing. The $D(h_k)$ cover $\mathrm{Spec}\, R$. On $D(h_k h_l)$ the two lifts $e_{h_k}$ and $e_{h_l}$ both restrict to $g_0$. Two lifts of the same map over a square zero thickening differ by a derivation, an element of $\mathrm{Hom}(g_0^* \Omega_{X/R}, I)$ over $D(h_k h_l)$, and these differences form a Čech 1-cocycle of a quasicoherent sheaf on the affine scheme $\mathrm{Spec}\, R_0$. Its class vanishes. Changing each $e_{h_k}$ by a 0-cochain, the lifts agree on the overlaps and glue to a section $e$ of $X$ over $R$, which lifts $e_0$. $\square$

With $X = A$ an abelian scheme and $e_0$ a point of $A_0$, the theorem lifts points of $A_0(R_0)$ to $A(R)$. With $X$ the scheme of homomorphisms of a smooth group, it lifts homomorphisms, when that scheme is smooth.

**Remark 1.17.6 (Formalization).** A tangent representation is `GlobalTheory.AbTan.TanRep` ([HopfLaurent.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HopfLaurent.lean#L30)), with lifting the unit `Lifts` and sum form `IsSum`. The cotangent sheaf is `GlobalTheory.LieVB.omega`, the conormal sheaf of the unit section, and $W_A$ is `Wmod`. The value $0$ in the second case of the Proposition is set by a classical `if` in `phiOf` ([ExistsTangentRepresentationSmoothGroupScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTangentRepresentationSmoothGroupScheme.lean#L131)), so $\Phi(z)$ is a junk value for $z$ that do not factor through some $v$. The two conditions of the Proposition are `GlobalTheory.TanRepr.cotangentAtUnit_tangentBijection` and its naturality, and the proof of the Theorem uses `GlobalTheory.T.exists_cotangent_frame_smooth_groupScheme`, `GlobalTheory.OmegaGlobal.isQuasicoherent_of_frames` and `GlobalTheory.T.finite_projective_cotangentGlobalSections_groupScheme`; the first paragraph of the proof of the Proposition describes what these give, and their proofs were not read. The Theorem asks only for a group, not a commutative one, and not for an abelian scheme. The Statement file of the second name imports Mathlib twice ([ExistsTangentRepresentationSmoothGroupSchemeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTangentRepresentationSmoothGroupSchemeStatement.lean#L1), lines 1 and 3). For the lifting of sections, the reduction to square zero is `GlobalTheory.T.smooth_section_lift_nilpotent_of_sqZero`, the local lifts are `GlobalTheory.T.exists_smooth_section_lift_basicOpen_affine` with the condition `LiftIn`, and the gluing is `GlobalTheory.T.exists_global_lift_of_chartLocal_lifts_squareZero`; the arguments given above for these three steps are the classical ones, and their proofs were not read.
