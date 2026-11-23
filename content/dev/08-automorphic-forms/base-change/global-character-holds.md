---
id: global-character-holds
title: The elliptic sum as a product of local twisted orbital integrals
kind: theorem
decl: PositivityTheory.Rg.BcB.G8.global_character_holds
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.ThetaNormCommutation.LocalComparisonSplitting.GlobalCharacterHolds
covers: 630
status: drafted
drafted_by: writer@claude
---
This theorem proves `G4`. It rewrites the elliptic part of the twisted trace formula on $\mathrm{GL}_a \times \mathrm{GL}_b$, an adelic sum of orbital integrals, as a sum over rational twisted classes of masses, archimedean characters, and products of local twisted orbital integrals at the finite places. It is a step below [EveryCharacter](/step/every-character/). Its result goes to `chainEx_holds` and `cmbEll_of`. The finite-place factorization comes from [`finHalf_holds`](/entry/fin-half-holds/).

## Statement

Let $E$ be a CM field in which each finite place is unramified over the maximal real subfield $F$. Fix Haar measures on $\mathrm{GL}_a(\mathbb{A}_E)$, $\mathrm{GL}_b(\mathbb{A}_E)$, $\mathrm{GL}_a(\mathbb{C})$ and $\mathrm{GL}_b(\mathbb{C})$.

The data:

- a set $S$ of finite places of $E$ with exactly one place above each finite place of $F$;
- translators $u_1 \in \mathrm{GL}_a(E)$, $u_2 \in \mathrm{GL}_b(E)$: $\theta_E(g) = u\, \bar g^{-T} u^{-1}$ for all $g$, and $u\, \bar u^{-T} = 1$, where $\theta_E$ is the twist used on the geometric side (conjugation by a fixed matrix $\Phi$, not unfolded);
- weights $l_1, l_2$ at the infinite places, numbers $\mathrm{val}_v$, and functions $\psi_v$ on $\mathrm{GL}_a(\mathbb{C}) \times \mathrm{GL}_b(\mathbb{C})$ whose twisted orbital integrals at regular elliptic pairs are $\mathrm{val}_v$ times the conjugate of a character value `chAt` (not unfolded) of the weights;
- test functions $\phi_1, \phi_2$, families of local functions at the finite places.

Let $\Phi_{\mathrm{ad}}$ be the adelic function built from $\psi$ at the infinite places and from $\phi_1$ (and $\phi_2$ at split places) at the places of $S$, after translation by $u_1, u_2$.

**Theorem.** There is $c \ne 0$, depending only on $E$, $a$, $b$ and the measures, such that

$$\sum_{(d_1, d_2)\ \text{reg. ell.}} O_{d_1, d_2}(\Phi_{\mathrm{ad}}) = c \prod_v \mathrm{val}_v \sum_{(\delta_1, \delta_2)} m(\delta_1) m(\delta_2)\, \chi_{l_1}(\delta_1) \chi_{l_2}(\delta_2) \prod_{w \in S} TO_w(\delta_1, \delta_2).$$

The left side is the elliptic sum of [the elliptic formula](/entry/ell-formula2-j/). On the right, $(\delta_1, \delta_2)$ runs over pairs of rational $\theta_E$-twisted classes whose norm polynomials $\det(X - \delta\theta_E(\delta))$ are separable with all roots of absolute value $1$. $m$ is the mass of the class, and $TO_w$ is the local twisted orbital integral at $w$ of $\phi_1$, or at a split place of the convolution of $\phi_1$ and $\phi_2$.

## Proof

The proof is one line: `global_character_of_finite_inputs` applied to three finite-place facts, `kfOC_holds` ($K_f$ is open and compact), `finLevel_holds` (the finite part has an open level), and `finHalf_holds`.

`global_character_of_finite_inputs` builds the term identity `Term`. This says that each orbital integral on the left equals $c \prod_v \mathrm{val}_v$ times the term of the class of $d u^{-1}$. It is proved by `termOf_holds` from eleven inputs, among them the three above. Then `global_character_of_holds` sums over classes. It uses `ClassBij`, a bijection of twisted classes $d \mapsto d u^{-1}$ that keeps regular ellipticity, together with `OrbInv`, `AdelCont` and `PolEq`.

## In the Lean code

The theorem is in [GlobalCharacterHolds.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/GlobalCharacterHolds.lean#L6). `G4` is in [IsTransl.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/IsTransl.lean#L82). The assembly is in [GlobalCharacterOfFiniteInputs.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/GlobalCharacterOfFiniteInputs.lean#L31).

The names `G4` and `global_character_holds` are used again for other statements in other namespaces, for example in `MemUnipBOfMemUnipotent.lean`. The folder name says "archimedean", but the inputs of this theorem are about the finite places.
