---
id: scalar-of-is-cob
title: One coordinate of an A_inf coboundary is near a crystalline cocycle
kind: theorem
decl: GlobalTheory.Cyc.ClassBound.scalar_of_isCob
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineExtensionClassBound
covers: 382
status: drafted
drafted_by: writer@claude
---
This lemma is the one-coordinate case of [the coordinate lemma](/entry/mem-hf-d-of-is-cob/). It composes a cocycle $f$ with values in a $\mathbb{Z}_\ell$-module $Y$ with an almost equivariant functional $\psi$. It checks the hypotheses of [the scalar step](/entry/scalar-step/) for $c = \psi \circ f$, and it turns the $A_{\inf}$ coboundary into the $B_{\mathrm{dR}}$ condition of that step. The work is in the scalar step.

## Statement

Notation as in [the coordinate lemma](/entry/mem-hf-d-of-is-cob/): $Y$, $\rho$, $f$, $e$, $N$, $s$, $K_s$, with the same hypotheses on $D$, $s$, $f$ and the $A_{\inf}$ coboundary. Let $\psi \colon Y \to \mathbb{Q}_\ell$ be $\mathbb{Z}_\ell$-linear with $|\psi(y)| \leq \ell^r$ and $|\psi(\rho(g)y) - \chi(g)^{-e}\psi(y)| \leq 1$ for all $g \in G_K$ and $y$.

Then there are a function $z \colon G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$ and $x \in B$ such that:

1. $z$ is a continuous cocycle on $G_{K_s}$ for the action $y \mapsto \chi(\sigma)^{-e} y$;
2. $z(\sigma) = \chi(\sigma)^{-e} \sigma(x) - x$ in $B$ for $\sigma \in G_{K_s}$;
3. $|z(g) - \ell^k \psi(f(g))| \leq 1$ for $g \in G_{K_s}$, with $k$ as in the coordinate lemma.

## Proof

Extend $\psi \circ f$ by $0$ to a function $c$ on $G_{\mathbb{Q}_\ell}$. On $G_{K_s}$ it has the three properties that the scalar step asks for:

- $|c| \leq \ell^r$, from the bound on $\psi$;
- $c$ is a cocycle up to $\mathbb{Z}_\ell$: $c(\sigma\tau) - c(\sigma) - \chi(\sigma)^{-e} c(\tau) = \psi(\rho(\sigma) f(\tau)) - \chi(\sigma)^{-e}\psi(f(\tau))$, since $f$ is a cocycle;
- $c$ is locally constant up to $\mathbb{Z}_\ell$: near $\sigma$, $f(\tau) - f(\sigma) \in \ell^r Y$, so $|c(\tau) - c(\sigma)| \leq 1$.

`PushCob.push_coboundary` turns the coboundary of $\ell^N (f \otimes 1)$ in $Y \otimes A_{\inf}/\xi^{e+1}$ into an element $b \in \mathrm{Fil}^0 B_{\mathrm{dR}}$ with $\ell^N c(\sigma) - (\chi(\sigma)^{-e}\sigma(b) - b) \in A_{\inf} + \mathrm{Fil}^{e+1} B_{\mathrm{dR}}$ for $\sigma \in G_{K_s}$. Then [`scalar_step`](/entry/scalar-step/) gives $z$ and $x$. The rest is bookkeeping.

## In the Lean code

The lemma is at [CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L201). The lemmas it calls:

- `GlobalTheory.PushCob.push_coboundary`, in ContractEquivariant.lean (statement read, proof not read);
- `scalar_step`, in the same file.

The value $0$ off $G_K$ is never used: every condition is on $G_{K_s} \subseteq G_K$. The hypothesis $K \subseteq K_s$ of the coordinate lemma does not appear here; only `hle`, $G_{K_s} \subseteq G_K$, is needed.
