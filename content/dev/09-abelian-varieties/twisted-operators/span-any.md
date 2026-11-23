---
id: span-any
title: Bounded holomorphic forms lie in the span of theta series, for any orthonormal source frame
kind: theorem
decl: GlobalTheory.AdSpan.span_any
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ThetaSpanAndGoodRange
covers: 937
status: drafted
drafted_by: writer@claude
---
This theorem says that a bounded automorphic function on a unitary group, of the right weight and level and killed by the lowering operators, is a finite linear combination of theta series. [`value_mem_span`](/entry/value-mem-span/) applies it to the value of a cusp form at an extremal vector. The theorem only changes the frame of the source space. The work is in [`span_std`](/entry/span-std/).

## Statement

Let $S$ and $T$ be Hermitian spaces over the CM field $E$ of ranks $n$ and $r$. Write $G_T(\mathbb R)$, $G_T(\mathbb A_f)$ and $G_T(\mathbb Q)$ for the archimedean, finite and rational parts of $G_T(\mathbb A)$ (`GinfC`, `GfC`, `GQ`). Let $\omega$ be a weak Weil representation of $G_S(\mathbb A) \times G_T(\mathbb A)$ on functions on $\mathrm{Mat}_{n \times r}(\mathbb A_E)$ (`IsWeak`), for a standard character $\psi$, with $g \mapsto (\omega(1,g)\Phi)(w)$ continuous (`ContT`).

**Theorem.** Assume:

1. $S$ has an orthonormal basis $b$, $n$ is even, $T$ has signature $(p_0,q_0)$ at each archimedean place, $4\,[E:\mathbb Q]\, r + 4 \le n$ and $r \le n$.
2. $M$ is a discrete series model on $T$ whose sign vector is positive exactly on the first $p_0$ coordinates, and $B_S(\tau)^*\,\mathrm{Gram}_\tau(S)\,B_S(\tau) = 1$.
3. $\Lambda_S$ is the lattice `L0c D S`, $\Lambda_T$ is self-dual, and $\beta_S$, $\beta_T$ are frames of them. $P_g \ne \emptyset$ and $Q$ are finite sets of places, none above $2$.
4. $f$ is a theta level vector (`IsThPVecOf`) for these data, and $\mathrm{pt}(P)$ is the Fock vector of $f$ for a polynomial $P$ (`pureTensorO`).
5. $U$ is a space of polynomials that contains $\Delta$ (`delta`, a product of powers of leading minors), with $\omega(h,1)\,\mathrm{pt}(U) \subseteq \mathrm{pt}(U)$ for $h \in G_S(\mathbb R)$.

Let $\varphi \colon G_T(\mathbb A) \to \mathbb C$ be bounded and left $G_T(\mathbb Q)$-invariant. Assume:

- $\varphi$ is smooth at the real places and killed by the lowering operators of the reversed basis of $M$ (`LowKilled`);
- each torus element $t_\tau(s)$ of that basis acts on $\mathrm{pt}(\Delta)$ and on $\varphi$ from the right by the same scalar;
- each $k \in G_T(\mathbb A_f)$ that stabilizes $\beta_T$ and reduces to $1$ at the places of $P_g$ fixes $f$ and $\varphi$.

Then

$$\varphi \in \operatorname{span}_{\mathbb C}\bigl\{\, g \mapsto (\omega(h,g)\,\mathrm{pt}(P))(0) \;:\; h \in G_S(\mathbb A),\ P \in U \,\bigr\}.$$

## Proof

1. `GlobalTheory.Ker.Inhab.inhabitants` builds a context $C$ on the reframed space $S' = $ `reS S b`, whose Gram matrix is $1$. Its lattice is related to $\Lambda_T$ by `IsAA`, which we did not unfold. The given $\psi$ and $\theta$ replace those of $C$.
2. `isB_onb`: the basis of $M$ is a good basis for $C$.
3. `T.exists_frameChange_weakWeilRepresentation` gives $e \colon G_{S'}(\mathbb A) \to G_S(\mathbb A)$, which keeps $G(\mathbb R)$, and a weak Weil representation $\omega'$ with $\omega'(h,g) \circ \mathrm{re} = \mathrm{re} \circ \omega(e(h), g)$.
4. `T.fockPolynomialVectors_reframeSource` and `T.reframe_vacuum_and_liftVector` move $B_S$, the Fock vectors and $f$ to $S'$, with a frame of the standard lattice.
5. [`span_std`](/entry/span-std/) gives the span statement on $S'$. Since $(\mathrm{re}\,\Phi)(0) = \Phi(0)$, the theta series for $(h,P)$ on $S'$ is the theta series for $(e(h),P)$ on $S$.

## In the Lean code

The theorem is at [ThetaSpanAndGoodRange.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaSpanAndGoodRange.lean#L158), and `isB_onb` is at line 138. We did not unfold `L0c`, `IsStdChar`, `DSModel` or `reF`. The hypothesis $\Lambda_S = $ `L0c D S` is used only in step 4. The invariance $\omega(1,k) f = f$ is a hypothesis here, not a conclusion.
