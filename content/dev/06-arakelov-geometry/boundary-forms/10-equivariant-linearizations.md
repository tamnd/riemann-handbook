---
title: Equivariant linearizations on a modification
decls:
  - GlobalTheory.EqvAct.equivariant_linearization_pullback
  - GlobalTheory.T.equivariant_linearization_pullback_compat
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Equivariant linearizations on a modification

[The theorem on the Hodge line bundle](/entry/hodge-line-bundle-rationally-linear/) says that the Hodge line bundle, pulled back to a normal projective modification $X'$ of $X_0$, is rationally linear for a finite group of level automorphisms that is unipotent modulo a neat prime. Its proof needs one input on the semi-abelian scheme itself: the group acts on the pullback of the semi-abelian scheme to $X'$, compatibly with the multiplication by $\mathcal{O}_E$, and the stabilizer of a point acts trivially on the fibre over that point. This section proves that input. The determinant of the Lie algebra of the pulled back scheme then carries the action, and this gives the rational linearization.

We keep the notation of [the section on separating orbits](/entry/separate-orbits-by-cusp/). Let $Y$ be the toroidal flag model of a family at level $j$, with coefficient field $F$, and let $Z$ be a component. Let $X_0$, $V_0$, $j_0 \colon V_0 \to X_0$ and $s_0$ be as there. The scheme $X_0$ is an open subscheme of the compactification of the model, and over this compactification there is a semi-abelian scheme $G$ with an action of $\mathcal{O}_E$ ([semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction)). Write $\iota_0 \colon X_0 \to \bar{X}$ for the inclusion into this compactification.

**Definition 2.10.1 (Group pullback).** Let $f \colon S' \to S$ be a morphism of schemes, let $G$ be a group scheme over $S$ and $G'$ a group scheme over $S'$. A morphism $\psi \colon G' \to G$ is a *group pullback along* $f$ if the square
$$\begin{array}{ccc} G' & \xrightarrow{\ \psi\ } & G \\ \downarrow & & \downarrow \\ S' & \xrightarrow{\ f\ } & S \end{array}$$
is cartesian and $\psi$ respects the group laws: for every $S'$-scheme $T$ and points $x, y \in G'(T)$, the product of $\psi(x)$ and $\psi(y)$ in $G(T)$, with $T$ seen over $S$ through $f$, is $\psi(xy)$.

So a group pullback identifies $G'$ with $G \times_S S'$ as a group scheme. An automorphism $\sigma$ of $S'$ and a morphism $m \colon G' \to G'$ form a group pullback along $\sigma$ when $m$ lies over $\sigma$ and is the induced isomorphism $G' \cong \sigma^* G'$ on points.

**Definition 2.10.2 (Equivariant linearization).** Let $X'$ be a scheme with a morphism $p \colon X' \to \bar{X}$ and an action $\rho'$ of a group $\Gamma$. An *equivariant linearization* of $G$ along $p$ for $\rho'$ consists of a group scheme $G'$ over $X'$ with a morphism $\psi \colon G' \to G$, an action of $\mathcal{O}_E$ on $G'$ and a map $m$ from $\Gamma$ to the endomorphisms of the scheme $G'$, such that:

1. $\psi$ is a group pullback along $p$, and $\psi$ commutes with the actions of $\mathcal{O}_E$;
2. each $m(\gamma)$ is a group pullback along $\rho'(\gamma)$, and commutes with the action of $\mathcal{O}_E$;
3. $m(\gamma_1 \gamma_2) = m(\gamma_1) \circ m(\gamma_2)$ for all $\gamma_1, \gamma_2 \in \Gamma$, where $\circ$ is composition of maps;
4. for every $\gamma$ and every point $x \in X'$ with $\rho'(\gamma)(x) = x$ as a morphism from the spectrum of the residue field $\kappa(x)$, the map $m(\gamma)$ is the identity on every $T$-point of $G'$ that lies over $\operatorname{Spec} \kappa(x)$.

Condition 4 says that the stabilizer of a point acts trivially on the fibre of $G'$ at that point. This is the condition that makes the induced action on the Lie algebra, and hence on its determinant, trivial on the fibres at fixed points, as the definition of a rational linearization requires.

**Theorem 2.10.3 (Equivariant linearization on a modification).** Assume the published Hodge bundle theorems. Let the datum have $p + q \ge 1$, let the level have $A = 1$, and let $F$ be algebraically closed in the function field of $Z$. Let $(I, g)$ be neat for $p + q$, with $I$ containing the level ideal. Let $\Gamma$ be a finite group with a homomorphism $\iota$ to the level automorphisms and an action $\rho$ on $V_0$, such that each $\iota(\gamma)$ is unipotent modulo $I$ and $\rho(\gamma)$ moves framed points by $\iota(\gamma)^{-1}$. Let $X'$ be an integral normal scheme with a morphism $\varphi \colon X' \to X_0$ such that $s_0 \circ \varphi$ is projective, an open immersion $\ell \colon V_0 \to X'$ with $\varphi \circ \ell = j_0$, and an action $\rho'$ of $\Gamma$ on $X'$ with $\ell \circ \rho(\gamma) = \rho'(\gamma) \circ \ell$ for all $\gamma$. Then $G$ has an equivariant linearization along $\iota_0 \circ \varphi$ for $\rho'$.

Lean: `GlobalTheory.EqvAct.equivariant_linearization_pullback` (also `GlobalTheory.T.equivariant_linearization_pullback_compat`, a second name).

*Proof.* Put $G' = G \times_{\bar{X}} X'$, the fibre product along $\iota_0 \circ \varphi$, with its projection $\psi$ to $G$ and the action of $\mathcal{O}_E$ by base change. Then $\psi$ is a group pullback and commutes with $\mathcal{O}_E$, which is condition 1. The rest is in three steps.

First, the action extends. Over $V_0$ the group $\Gamma$ acts on the universal abelian scheme: $\rho(\gamma)$ moves framed points by $\iota(\gamma)^{-1}$, and the level automorphism $\iota(\gamma)$ gives an isomorphism of the abelian schemes over a point and over its image. Since $X'$ is integral and normal, $s_0 \circ \varphi$ is projective and $\ell(V_0)$ is a dense open subscheme of $X'$, these isomorphisms extend from $\ell(V_0)$ to $X'$. This gives, for each $\gamma$, a map $m(\gamma)$ that is a group pullback along $\rho'(\gamma)$, commutes with $\mathcal{O}_E$ and agrees with the level action over $V_0$, and the rule $m(\gamma_1 \gamma_2) = m(\gamma_1) \circ m(\gamma_2)$ holds. These are conditions 2 and 3.

Second, the action is controlled on torsion. Because $(I, g)$ is neat and $I$ contains the level ideal, the $I$-torsion of $G'$ is tied to the level module modulo $I$, and $m(\gamma)$ acts on it through $\iota(\gamma)$.

Third, the fibres at fixed points. Let $\rho'(\gamma)$ fix the point $x$. Then $m(\gamma)$ is an automorphism of finite order of the fibre $G'_x$, and by the second step it acts on the $I$-torsion through $\iota(\gamma)$, which is unipotent modulo $I$. The neatness of $(I, g)$, with $g$ a prime larger than $p + q + 1$, then forces $m(\gamma)$ to be the identity on every point of $G'$ over $x$. This is the mechanism of Serre's rigidity lemma for level structures. It is condition 4. $\square$

The theorem is used once, in the proof of [the theorem on the Hodge line bundle](/entry/hodge-line-bundle-rationally-linear/). There the determinant of the Lie algebra of $G'$ along the eigenspaces of $\mathcal{O}_E$ is $\varphi^* \delta$, and the action $m$ gives the cocycle $c$ of the rational linearization; condition 4 gives the condition at fixed points.

**Remark 2.10.4 (Formalization).** The three steps are three separate results: `GlobalTheory.T.equivariant_action_eq_of_agree_on_generators` (the extension of the action), `GlobalTheory.T.torsion_fibre_injects_levelModule` (the torsion step, which uses neatness) and `GlobalTheory.T.fibre_action_trivial_of_fixed_point_residue_field` (the fixed point step, which uses unipotence). We have not unfolded their inner definitions `IsEqvAct`, `MovesEta` and `TorsLevel`, nor their proofs, so the proof above gives what the three statements say, with the reasons suggested by their hypotheses; we have checked only the statements. The hypothesis that $F$ is algebraically closed in the function field is introduced and never used ([EquivariantLinearizationPullbackCompat.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/EquivariantLinearizationPullbackCompat.lean#L22)). The second name at line 44 is proved by `first | exact ...` from the first. Condition 3 is written in the order $m(\gamma_1 \gamma_2) = m(\gamma_2) \gg m(\gamma_1)$, which is composition in diagrammatic order.
