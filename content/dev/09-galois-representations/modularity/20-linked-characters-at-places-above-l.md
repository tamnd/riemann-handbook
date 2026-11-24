---
title: Linked characters at places above l
decls:
  - UpperTheory.V.Z.J.tan
  - UpperTheory.V.J.tanA_of
  - UpperTheory.V.J.tanA
  - UpperTheory.Gal.projectedFormsSystemPart.red2_alt
  - UpperTheory.Gal.projectedFormsSystemPart.linkedUnlE_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Linked characters at places above l

This section proves that the irreducible three-dimensional points of the unitary family of case V are unlinked at the places above $l$ where they are potentially crystalline. Two inertia characters $\psi_i$ and $\psi_j$ at a place $v$ are linked if $\psi_i = \psi_j \cdot \chi_{\mathrm{cyc}}$ on the decomposition group at $v$. A linked pair is the local shape of a reducible point, and the count V of the next section uses unlinkedness to show that the points it counts are rigid and well separated from the residual point. The proof is by contradiction. A linked pair at a point $\xi$ gives two independent tangent directions at $\xi$ that do not move the weights. The modularity of Hida families of section 19 and the density of good points show that the Hida ideal dies near $\xi$. The end statement for Hida families then forbids two such directions.

We use a Galois frame $\Phi$: a profinite group $\Gamma$ (a Galois group of $\mathbb{Q}$ with restricted ramification), a set $\Phi_V$ of places above $l$, for each $v \in \Phi_V$ a decomposition group $G_v$ with inertia subgroup $I_v$ and a map $G_v \to \Gamma$, and the cyclotomic character $\varepsilon$. A deformation space of rank three for $\Phi$ over a complete local ring $\mathcal{O}$ is a complete local $\mathcal{O}$-algebra $R$ with a representation $\rho \colon \Gamma \to \mathrm{GL}_3(R)$ that is upper triangular on each $G_v$, with diagonal characters $\psi_{v,0}, \psi_{v,1}, \psi_{v,2} \colon G_v \to R^{\times}$, and with the universal property for such lifts of a fixed residual representation.

**Definition 8.20.1 (Weight-fixing derivation).** Let $\xi \colon R \to \mathcal{O}$ be a point. A weight-fixing derivation at $\xi$ is an $\mathcal{O}$-linear map $\delta \colon R \to \mathcal{O}$ with

$$\delta(ab) = \xi(a)\, \delta(b) + \xi(b)\, \delta(a), \qquad \delta(\psi_{v,j}(s)) = 0$$

for all $a, b \in R$, all $v$, all $j$ and all $s \in I_v$.

These are the tangent vectors at $\xi$ along which the inertia characters, and so the Hodge-Tate weights, stay fixed. In a Hida family finite over the weight space, there are no such tangent vectors on the family itself.

**Definition 8.20.2 (Unit step).** Let $\rho_\xi$ be the specialization of $\rho$ at $\xi$, let $v \in \Phi_V$ and $i \in \{0, 1\}$. We say that $\rho_\xi$ has a unit step at $(v, i)$ if, after conjugation by some $g \in \mathrm{GL}_3(\mathcal{O})$, the restriction $t$ of $\rho_\xi$ to $G_v$ is upper triangular with diagonal entries $\psi_{v,j}$, if $t_{ii} = \varepsilon\, t_{i+1, i+1}$, and if there are continuous maps $u, \beta \colon G_v \to \mathcal{O}$ such that $u$ is a homomorphism, $u$ vanishes on $I_v$, $u \ne 0$, and

$$\beta(s s') = \beta(s) + \varepsilon(s) \beta(s') - t_{i, i+1}(s)\, t_{i+1, i+1}(s)^{-1} u(s').$$

So the two diagonal characters at the step are linked, and the off-diagonal entry between them is tied to a nonzero unramified homomorphism $u$. The class $u$ is the unramified direction in which we will deform.

**Lemma 8.20.3 (Two weight-fixing derivations).** Let $\mathcal{O}$ be a discrete valuation ring finite over $\mathbb{Z}_l$ with $l \ne 0$ in $\mathcal{O}$. Let $\Phi$ be a frame with the size bound $C_0$, with complex conjugations $c_w$ at the infinite places with $c_w^2 = 1$ and $\varepsilon(c_w) = -1$, and with the global and local conditions of the frame. Let $(R, \rho)$ be a deformation space of rank three, $\xi$ a point, and assume that $\rho_\xi$ has a unit step at $(v, i)$. Then there are two weight-fixing derivations at $\xi$ that are linearly independent over $\mathcal{O}$.

Lean: `UpperTheory.V.Z.J.tan`.

*Proof.* The point $\xi$ gives a lift of the residual representation, and we put its local restrictions in a box: a family of upper triangular forms at the places of $\Phi_V$, compatible with $\rho_\xi$. The unit step modifies the box at $(v, i)$: the homomorphism $u$ and the map $\beta$ deform the entries $t_{ii}$, $t_{i,i+1}$ and $t_{i+1,i+1}$ while the inertia characters stay fixed. A Selmer bound, from the global and local conditions of the frame and the odd complex conjugations, gives a constant $C$ such that, for each $k$, the space of cocycles modulo $l^{k}$ of the box with fixed inertia characters has length at most $C$ plus the length of the deformations of the box. The deformations of the box modulo $l^{k}$ grow with $k$ in two independent directions, the one of $u$ and the one of a conjugation of the step. A rank count modulo $l^{k}$ for all $k$ then gives two weight-fixing derivations $\delta, \delta'$ at $\xi$ that are linearly independent. $\square$

Now we work in the setting of case V. Let $N$ be even, $e \ge 1$, $\psi$ a Dirichlet character modulo $N$, $\eta$ the quadratic character of a CM field $K$ of degree two, and $\Psi$ the character $\chi_{\mathrm{cyc}}^{e} \psi$ of section 17. A Galois link $k$ over a CM field $L$ is a frame $\Phi$ for $G_L$ with the maps that identify its places and its decomposition groups with those of $G_{\mathbb{Q}}$. A real family $R$ for $k$ consists of a Hida setting over $L$ with universal ordinary determinant ring $B_0$, a deformation space $(S, \rho)$ of rank three for $\Phi$, and a twisting character $\kappa$, with the conditions that relate them.

**Theorem 8.20.4 (Linked characters give two derivations).** Assume the cohomology hypotheses and the local published theorems. Let $R$ be a real family for a Galois link of case V, let $\xi$ be a point of the deformation space, and let $r = \rho_\xi$ be irreducible, with inertia characters $\psi_{v,i} = \Psi^{w_i}$ on $I_v$ for the weights $w_i$ of rank three. Let $v$ be a place above $l$ at which $r$ is potentially crystalline, and suppose that, for some $i$ and $j$, $\psi_{v,i}(g) = \psi_{v,j}(g)\, \chi_{\mathrm{cyc}}(g)$ for all $g \in G_v$. Then there are two weight-fixing derivations at $\xi$ that are linearly independent.

Lean: `UpperTheory.V.J.tanA` (also `UpperTheory.V.J.tanA_of`, with the unit statement and the equality of degrees as hypotheses).

*Proof.* Potential crystallinity at $v$ and the local published theorems give a unit step: the linked pair $(i, j)$ is a step $(v, i')$ of the upper triangular form, and the extension class between the two linked characters, which is crystalline, has the form required of a unit step. The equality of degrees gives the size bound $C_0$ of the frame, and the link $k$ gives the complex conjugations, odd for $\varepsilon$. The cohomology hypotheses give the global and local conditions of the frame. Now the [Lemma 8.20.3](/entry/tan/) on two derivations applies. $\square$

**Definition 8.20.5 (Local death).** Let $\varphi \colon B_0 \to S$ be a surjection, $J$ an ideal of $B_0$ and $\xi$ a point of $S$. The ideal $J$ dies locally at $\xi$ if for each $a \in J$ there is $s \in S$ with $\xi(s) \ne 0$ and $s \varphi(a) = 0$.

So $J$ is zero in the local ring of $S$ at $\xi$. Then the family $B_0/J$ and the deformation space $S$ agree near $\xi$.

**Theorem 8.20.6 (The Hida ideal dies locally).** Assume global Artin reciprocity and the main case of the dense threshold argument. Let $R$ be a real family for a Galois link of case V over a large coefficient ring, with twisting character $\kappa$ of the required shape. Let $\varphi \colon B_0 \to S$ be a surjection compatible with the representations, and $J$ an ideal of $B_0$ such that every point of $S/\varphi(J)$ is good, $B_0/J$ has the expected dimension, the arithmetic points of $B_0/J$ are dense, and the end points of $R$ are nice. Then $J$ dies locally at each integral point $\xi$ of $S$ of type I.

Lean: `UpperTheory.Gal.projectedFormsSystemPart.red2_alt`.

*Proof.* Global Artin reciprocity gives a weight $h$ at which the arithmetic points of $S$ lie over $B_0$, with free weight space. The density of arithmetic points of $B_0/J$ and the dimension $1 + 3d$, where $d$ is the number of places of the frame, give the density of good points in $S/\varphi(J)$. At each good point $\zeta$, the nice end points make $\zeta$ nice, and the main case of the dense threshold argument gives the fixed point property at $\zeta$, which bounds the local ring of $S$ at $\zeta$ by that of $S/\varphi(J)$. Since $B_0$ is Noetherian, an abstract reduction lemma passes from the dense set of good points, where this bound holds, to every integral point of type I. So $J$ dies locally at $\xi$. $\square$

**Theorem 8.20.7 (Points of case V are unlinked).** Assume global Artin reciprocity, local class field theory at all places, the modularity of unitary Hida families, the [Theorem 8.19.4](/entry/modularity-n-of-printed-mult-comp/) on modularity in rank three, the existence of levels, of weights and of the promodular ring, unitary three-dimensional automorphy, the seed in rank two, the twist and algebraicity conditions, the [Theorem 8.20.4](/entry/tan-a/) on two derivations, and the main case of the dense threshold argument. Let $N$ be even, let $L$ be a CM field, let $\Phi$ be a frame with the size conditions, and let $k$ be a Galois link of case V with a seed. Let $A$ be a discrete valuation ring finite over $\mathcal{O}$, let $\rho$ be a lift over $A$ of the residual representation of rank three with inertia characters $\Psi^{w_i}$, and let $r$ be the attached representation of $G_L$ over $\overline{\mathbb{Q}}_l$. Assume that $r$ is irreducible on every open subgroup. Then at each place $v$ of $\Phi$ at which $r$ is potentially crystalline, and for all $i$ and $j$, there is $g \in G_v$ with

$$\psi_{v,i}(g) \ne \psi_{v,j}(g)\, \chi_{\mathrm{cyc}}(g).$$

Lean: `UpperTheory.Gal.projectedFormsSystemPart.linkedUnlE_alt`.

*Proof.* Suppose that $\psi_{v,i} = \psi_{v,j} \chi_{\mathrm{cyc}}$ on $G_v$. The seed and the inputs give a real family $R$ over a larger coefficient ring, with an ideal $J$ of $B_0$ for which the Hida family is modular, the multiplicity comparison holds, the arithmetic points are dense and the end points are nice, and with a surjection $\varphi \colon B_0 \to S$. The lift $\rho$ is a point $\xi$ of $S$, and $r$ is its specialization; $\xi$ is of type I, and by global Artin reciprocity it lies over an arithmetic point of $B_0$ of some weight $w$ that is irreducible. By the [Theorem 8.20.4](/entry/tan-a/), there are two independent weight-fixing derivations at $\xi$. By the [Theorem 8.20.6](/entry/red2-alt/), $J$ dies locally at $\xi$. The unramified algebraic weights statement, with the density and the multiplicity comparison, makes $B_0/J$ unramified at $J$. The end statement for Hida families says that, at an irreducible arithmetic point of type I where an unramified ideal dies locally, two weight-fixing derivations are never linearly independent. This is a contradiction. $\square$

**Remark 8.20.8 (Formalization).** Two declarations are named `linkedUnlE_alt`: the one of this section, in [UnitaryRankTwoFlags.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/UnitaryRankTwoFlags.lean#L116), and a wrapper in the namespace `UpperTheory.V.Z.J` that takes the extended hypotheses and passes their parts to it. The unlinkedness statement `LinkedUnlE` and its conclusion `UnlPt` are in [LinkedUnlEOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/LogarithmicNormBounds/LinkedUnlEOf.lean#L12) and [AdmissibleUnitaryThreePoint.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/WeightInfinitesimalCharacters/AdmissibleUnitaryThreePoint.lean#L20); the quantifier over $i$ and $j$ includes $i = j$. The end statement is `End` in [AbsGood.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/AbsGood.lean#L90). The unit step is `UnitStep` in [UnitStep.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/CrystallineCardinalities/UnitStep.lean#L50). The steps of the derivation lemma (`box_pt`, `box_unit`, `selLow`, `rankTwo`) and of the local death theorem (`wtEx`, `niceAt2_alt`, `fixOf_alt`, `denseOf`, `redAbs`, `fixLe`) are summarized from their statements; we have not unfolded the frame conditions `Ok`, `GWL` and `LocE`, the real family `CReal`, or `EndPtAlt`.
