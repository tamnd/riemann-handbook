---
title: Models of deformation rings and the trace inequality
decls:
  - UpperTheory.V.GradeZeroInterpolatingElement.exModel
  - UpperTheory.V.GradeZeroInterpolatingElement.galoisRep_ineq_of_allIrreducible_nonvanishing
  - UpperTheory.V.U3.exists_model
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Models of deformation rings and the trace inequality

This section proves that a reducible four-dimensional symplectic Galois representation has a *model*: a graded complete local ring with a smooth point, whose quotient by explicit equations of known weights is a deformation ring of the representation. With the model, we bound the length of a Tate-Shafarevich group by the traces of irreducible lifts. This is the inequality of the Ribet method: if the group is large, then there are many irreducible lifts whose traces are close to the traces of the reducible representation. The trace inequality feeds [Theorem 8.17.7](/entry/main-big/). The same construction for unitary groups of rank three gives a model for [Theorem 8.22.2](/entry/one-char-unram-u/). The background is in [deformation functors](/learn/deformations-patching/#deformation-functors), [symplectic groups](/learn/groups/#general-linear-and-symplectic-groups) and [Galois representations](/learn/galois-representations/#galois-representations).

### Reducible symplectic data

Let $l$ be a prime and $O$ a complete discrete valuation ring finite over $\mathbb{Z}_l$ with residue field $k$, and let $\chi_O$ be the cyclotomic character with values in $O$. Fix a finite set $S$ of primes, an integer $e$, and characters $\psi, \xi, \omega : G_\mathbb{Q} \to O^\times$. Put
$$\begin{aligned} \Psi &= \chi_O^{e} \psi , & \alpha &= \chi_O \, \omega^{-1} \xi , \\ \beta &= \Psi \alpha^{-1} , & \theta &= \alpha \Psi , \end{aligned}$$
and let $r_0 = \mathrm{diag}(\theta, \Psi, \alpha, 1)$. It is a representation into $\mathrm{GSp}_4(O)$ with multiplier $\theta$, and its Hodge-Tate weights are $e + 1, e, 1, 0$ in this order. Let $\bar r_0$ be its reduction. Let $S_b$ be the set of primes $p \neq l$ in $S$ such that $l$ divides the order of $\psi$ on the inertia at $p$, and put $T = \{l\} \cup S_b$.

**Definition 4.8.1 (Good symplectic data).** The data are *good* if $l$ is odd, $2$ and $l$ lie in $S$, $e \geq 2$, $\Psi(c) = 1$ for a complex conjugation $c$, $\omega^{l-1} = 1$ and $\omega \equiv \chi_O$ modulo the maximal ideal, $\xi$ has order prime to $l$, is unramified at $T$ and has $\xi(c) = -1$, and the chosen Frobenius elements and the element $g_0$ satisfy the genericity conditions; among them, $\bar\alpha(g_0) \neq 1$, $\bar\Psi(g_0) \neq 1$, and the characters $\alpha$, $\beta$, $\theta$ and their inverses have vanishing cohomology in the sense of the data.

A *point* is a continuous representation $r : G_\mathbb{Q} \to \mathrm{GSp}_4$ over the algebraic closure $\overline{\mathbb{Q}}_l$ that lifts $\bar r_0$, has multiplier $\theta$, is unramified outside $T$, is ordinary at $l$ with the weights above, satisfies the conditions at $S_b$, and is normalized at a chosen Frobenius element. Put
$$a_g(r) = \mathrm{tr}\, r(g) - \mathrm{tr}\, r_0(g) .$$
Let $\mathrm{Sha}$ be the length over $O$ of the Tate-Shafarevich group of the twist by $\Psi^{-1}$ at level $\prod_{p \in S} p$, as in the Section on Bernoulli bounds, and let $\mathrm{nrm}(\mathrm{Sha})$ be this length divided by the ramification index of $O$.

**Definition 4.8.2 (Trace inequality).** For $g \in G_\mathbb{Q}$, the *trace inequality* at $g$ holds if $\mathrm{Sha}$ is finite and there is a finite set $\Xi$ of irreducible points, pairwise not conjugate, with
$$\mathrm{nrm}(\mathrm{Sha}) \log l \leq 2 \sum_{r \in \Xi} - \log | a_g(r) | .$$

### Models

The torus of diagonal matrices in $\mathrm{GSp}_4$ acts on the lifts of $r_0$ by conjugation. Its characters give a grading by $\mathbb{Z} \times \mathbb{Z}$, in which the entry $(i,j)$ has a weight $\mathrm{wt}(i,j)$.

**Definition 4.8.3 (Model).** A *model* for good symplectic data consists of:

1. a complete local domain $R$ over $O$ with a grading by $\mathbb{Z} \times \mathbb{Z}$ and an origin, smooth at a point of tangent dimensions $(r, r', m)$;
2. $r + 1$ elements $F$ of weight $-\lambda$, $r'$ elements $E$ of weight $\lambda$ and $m$ elements $Z$ of weight $0$, where $\lambda$ is the weight of the extension class;
3. a lift $\rho$ to $R/(F, E, Z)$ which is a point in the sense above and is universal: its entries generate the ring;
4. the entries of $\rho$ are homogeneous of weight $\mathrm{wt}(i,j)$, and the origin maps $\rho$ to $r_0$;
5. for each cocycle $z$ of $\Psi^{-1}$ modulo $a$, unramified outside $T$ with $z(g_0) = 0$, a derivation of weight $\lambda$ whose values on the entries $(2,0)$ and $(3,1)$ are $\theta z$ and $\Psi z$.

The equations $F$, $E$ and $Z$ cut the deformation ring out of a smooth graded ring, and their weights are what the trace inequality counts. Condition (5) ties the cocycles of the Tate-Shafarevich group to tangent directions of the model.

**Theorem 4.8.4 (Existence of models).** Assume the cohomological input on local presentations. Let the symplectic data be good, assume the condition on the field of $\ker \bar r_0$, and assume the dimension formulas: the local tangent space in weight $j$ has dimension $\dim H^1_c + 2$ for $j = 0$, $\dim H^1_c + 1$ for $j = \pm \lambda$, and $\dim H^1_c$ otherwise, with $H^1_c = 0$ in the other weights. If the local deformation ring at $T$ has a graded presentation with a smooth point, then the data have a model.

Lean: `UpperTheory.V.GradeZeroInterpolatingElement.exModel`.

*Proof.* The local data at the places of $T$ give a frame of local presentations: a graded smooth ring for the local deformation problem at $l$ and one for each place of $S_b$, with a smooth point of dimension $\dim L + \# S_b \cdot \dim P$. The global deformation ring is a quotient of the completed tensor product of the local rings, with a relative presentation over it. The cover of a relative presentation at a smooth point gives a graded complete local domain $R$, smooth at a point, with the global relations. Pass to the associated graded ring to keep the grading. The relations split by weight. There are six root pairs of odd weight, four of them in the unipotent radical of the Klingen parabolic and two in the Siegel parabolic (this split is our reading; the Lean proof does not name the parabolics), and the dimension formulas give the count of relations in each weight. The relations of weight $-\lambda$, $\lambda$ and $0$ are the families $F$, $E$ and $Z$, and their sizes $r + 1$, $r'$ and $m$ follow from the global Euler characteristic count with $\# T = \# S_b + 1$. The derivations come from the action of the cocycles on the tangent space in weight $\lambda$. $\square$

### The trace inequality

**Theorem 4.8.5 (Trace inequality).** Let the symplectic data be good with a model. Assume the commutative algebra inputs on graded rings with orbit covers, the local published theorems, the vanishing of the Selmer group in characteristic zero, the finiteness of the Selmer group, and these three conditions: the space of points over the closed fibre is finite, no point has extra endomorphisms, and every irreducible point is infinitesimally rigid in $\mathfrak{sp}_4$. Let $g \in G_\mathbb{Q}$ with $a_g(r) \neq 0$ for every irreducible point $r$. Then the trace inequality at $g$ holds.

Lean: `UpperTheory.V.GradeZeroInterpolatingElement.galoisRep_ineq_of_allIrreducible_nonvanishing`.

*Proof.* The model gives an element $a$ of the graded ring of weight zero whose value at each point $x$ is $a_g(\rho_x)$. The points of the model over $\overline{\mathbb{Q}}_l$ give a family of representations; conjugate representations come from points in the same orbit of the torus. By the finiteness, the absence of extra endomorphisms and the rigidity, the orbits of irreducible points are finite and reduced. The commutative algebra input on orbit covers applies to the ring with equations $F$, $E$, $Z$ and the element $a$. It gives a cover of the orbits and a bound for the cotangent length:
$$\mathrm{cot}(-\lambda) \leq \frac{2 \, e_O}{\log l} \sum_{x} - \log | a(x) | ,$$
where the sum is over a set of points, one in each orbit of a minimal cover, and $e_O$ is the ramification index. Let $\Xi$ be the set of representations of these points; they are irreducible and pairwise not conjugate. The derivations of the model are injective on the cocycles, so the second input bounds the length of the Tate-Shafarevich group by the cotangent length in weight $-\lambda$, and this length is finite. Dividing by $e_O$ gives the trace inequality. $\square$

The inequality has the form of the lower bound of Ribet's method: the length of a Selmer group is at most the length of the congruence module between the reducible point and the irreducible points, and the congruence module is measured by the valuations of $\mathrm{tr}\, r(g) - \mathrm{tr}\, r_0(g)$.

### Models for unitary groups of rank three

The same construction applies to a representation of $G_K$ for an imaginary quadratic field $K$, polarized by the character $\eta$ of $K$, with values in $\mathrm{GL}_3$.

**Definition 4.8.6 (Unitary data).** *Unitary data* consist of an imaginary quadratic field $K$ with character $\eta$, a place $\iota : G_{\mathbb{Q}_l} \to G_\mathbb{Q}$, an integer $e$, a Dirichlet character $\psi$ modulo $N$ with values in $O$, and $\Psi = \chi_O^e \psi$. An element $g_1 \in G_\mathbb{Q}$ is *marked* if $\eta(g_1) = 1$ and $\Psi(g_1)^2 - 1$ is a unit. For a local condition $U$ at $l$ and a marked $g_1$, the *ring* of the data is the universal ring of polarized lifts of $\Psi \oplus 1 \oplus \Psi^{-1}$ with the local condition $U$, normalized at $g_1$.

A model of such a ring is a graded ring with a point, equations of known weights and a smooth point, a surjection onto the ring whose kernel is the ideal of the equations, homogeneous entries, the density of points, derivations and lifts, in the same form as above.

**Theorem 4.8.7 (Models for unitary groups).** Assume the cohomological inputs: the local conditions, Poitou-Tate duality, the global finiteness, the global Euler characteristic formula and the Kolyvagin bound of the Section on Gauss sums. Assume the cohomological input on local presentations. Then for unitary data, a local condition $U$ at $l$, a marked element $g_1$ and the ring $S$ of these data, $S$ has a model over $\overline{\mathbb{Q}}_l$.

Lean: `UpperTheory.V.U3.exists_model`.

*Proof.* The data give $\eta$, $\Psi$ and $K$ with the expected properties. The local conditions are good at the places of the level. The universal ring exists, since the residual representation has only scalar endomorphisms that commute with the polarization and the finiteness of the cohomology gives the $\Phi$-condition on the field of $\ker \bar\Psi$. Its local presentation at the places of the level exists by the local input. A presentation of $S$ over it, with the count of relations from the Euler characteristic formula, gives the model, and a box presentation of the graded ring gives the smooth point. $\square$

**Remark 4.8.8 (Formalization).** The inputs `LemmaP`, `LemmaM`, `LemmaM'`, `Loc.LocalPublishedTheorems`, `SoV`, `SoFin` and `CohInp` are hypotheses, and `LemmaP` is not unfolded here; `LemmaM` and `LemmaM'` are in `CommutativeAlgebra/OrbitVanishingLocal.lean` (lines 111 and 120). The good conditions are the structure `Good` in `SymplecticGSp4/DecompSigmaOrd.lean` (line 94); the text lists the conditions it uses and does not unfold the genericity conditions on Frobenius elements. The theorem `exModel` is in [ExModel.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/ExModel.lean#L425) and the trace inequality in [GaloisRepIneqOfAllIrreducibleNonvanishing.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/GaloisRepIneqOfAllIrreducibleNonvanishing.lean#L152); both use the namespace `GradeZeroInterpolatingElement`, whose name does not describe them, and both are stated with full names. The Lean statement of the trace inequality quantifies over the model and lists the rigidity condition as `D.AllIrr D.RigidAt`. The weight count in the proof of `exModel` is through the private lemma `tower` (line 37) and the lemmas `p6`, `p4` and `p2` (lines 155 to 157), which the text summarizes. The unitary theorem is in [ModelEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/ModelEx.lean#L156). Its data `Dat` (`UnitaryThreeGroups/RhoKApply.lean`, line 16) has the same short name as an unrelated `Dat` in `PrimitiveFrobeniusFixed/IsAdmissiblePrimeListNil.lean` (line 128). The model structure for the unitary case is in `ConjStable.lean` (line 54), a module named after another notion.
