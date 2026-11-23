---
id: t-good-tower-real-extra
title: A flat root line of bounded height on each component (statement form)
kind: theorem
decl: GlobalTheory.T.good_tower_real_extra
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerRealExtraStatement
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [the relay](/entry/relay-good-tower-real-extra/), and its proof applies the relay. The content is further down, in [`global_model_tower_final_condition`](/entry/global-model-tower-final-condition/) and [`rootFlatOnHodge`](/entry/root-flat-on-hodge/). In [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/), it gives the bound `PropF` with constant $4$, together with `PropFTop_holds`.

## Statement

Use the notation of [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/). Let $M$ be a root model and $\tau \in \Psi$. A *flat root line* $R$ for $(M, \tau)$ is:

- a number field $F$ with a map $\varphi$ into the field $\Omega$ of the coordinates of $M$ that sends $\mathcal{O}_F$ into the integral charts of $M$;
- a smooth hermitian line $\overline A$ whose degree is $\sum_i \deg x_{\tau,i}$;
- a flat structure on $\overline A$ over $\varphi$: a multihomogeneous ratio $f/g$ of degree $m \cdot \deg A$ for some $m \geq 1$, and constants $\kappa_\sigma > 0$ for the embeddings $\sigma \colon F \to \mathbb{C}$, invariant under conjugation, with $|f(z)| = (\kappa_\sigma \|\cdot\|_A(z))^m |g(z)|$ at the points $z$ over $\sigma$;
- smooth functions $v_t$ with $\prod_i \|\cdot\|_{x_{\tau,i}(t)} = \|\cdot\|_A\, e^{-v_t}$, such that the integrals of $v_t$ against the top monomials in the lines of $M$ tend to $0$ as $t \to 0^+$.

Its height is $h(R) = -\frac{1}{[F:\mathbb{Q}]} \sum_\sigma \log \kappa_\sigma$.

A real number $h$ is *near the record* for $N$, a finite set of primes $S$, $r > 0$ and $L \in \mathbb{R}$ if $h = h_0 + \sum_{p \in S} d_p$ with
$$|h_0| \leq N\big(\tfrac32 \log r + \tfrac12 |L|\big), \quad |d_p| \leq \Big(\frac{N}{p-1} + N v_p\Big) \log p,$$
for some $v_p \geq 0$ with $\sum_{p \in S} v_p \log p \leq \log r$. Then $|h| \leq N\big(\tfrac52 \log r + \tfrac12|L| + \sum_{p \in S} \frac{\log p}{p-1}\big)$.

**Theorem.** Assume `FlatDegree` and $\mathrm{Given}$. Let $E$, $H$, $D$ with $p, q \geq 1$, $Y$, $T$, $o$ and $II$ be as in [the height bounds](/entry/good-tower-i5/). Then for each component $c$ and each $\tau$, the root model $M_{2,c}$ has a flat root line $R$ for $\tau$ whose height is near the record for $N = p + q$, the bad primes of $T$, $r = \mathrm{rd}_E$ and $L = \operatorname{Re} L'/L(1, \chi)$.

## Proof

Apply `Relay.good_tower_real_extra`.

## In the Lean code

The theorem is in [GoodTowerRealExtraStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerRealExtraStatement.lean#L16). `RootFlat`, its height and `NearRecord` are in [NumberField.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/NumberField.lean#L12). The flat structure is `FlatHerm` in [ExistsPowSubMemSpanOfIsUnitModOfIsAlgClosed.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ExistsPowSubMemSpanOfIsUnitModOfIsAlgClosed.lean#L37). `hostRd` and `hostLval` are in [TowerOrigin.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/TowerOrigin.lean#L121). The bound on $|h|$ is our arithmetic from `NearRecord`.

The names "real" and "extra" do not describe the conclusion, which is a height bound for a flat line on each component. The conclusion does not involve $II$.
