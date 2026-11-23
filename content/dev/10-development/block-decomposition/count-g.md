---
id: count-g
title: The twisted trace on a K-type as a sum over highest weights
kind: theorem
decl: GlobalTheory.CompanionTheory.RealCountG.countG
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.DiagonalMemUnitary
covers: 379
status: drafted
drafted_by: writer@claude
---
This theorem is the counting step of [`coreG`](/entry/core-g/). It writes the twisted trace of $A$ on the multiplicity space of a $U(n)$-type as $2^n$ times a sum of traces of $A$ on spaces of highest weight vectors. Its parent [`countG_holds`](/entry/count-g-holds/) is a second name for it. The proof splits the multiplicity space by the highest weights of $E^\vee$ and computes the trace of $T^\vee$ on each piece by Weyl characters (see [highest weights](/learn/representations/#highest-weights-and-branching)).

## Statement

We use the notation of [`coreG`](/entry/core-g/): $\lambda$, the representation $E$ of $U(n)$ with $T$ (`IsLefK`), the module $V$ with $E^1$, $E^2$, $\sigma$, $A$ (`IsCoreMod`), the space $\mathrm{Hom}_{U(n)}(E^\vee, V)$ with the action $t \mapsto A \circ t \circ T^\vee$, and the finite set $H$ of weights $2\lambda + 2r$. For a weight $\mu$, let $V_\mu$ be the space of $v \in V$ with $K_{aa} v = \mu_a v$ and $K_{ab} v = 0$ for $a < b$, where $K = E^1 + E^2$.

**Theorem** (`CountG`). Suppose that $\mathrm{Hom}_{U(n)}(E^\vee, V)$ is finite-dimensional. Then:

1. for each $\mu \in H$, $V_\mu$ is $A$-stable and finite-dimensional;
2. if $\mathrm{Hom}_{U(n)}(E^\vee, V) \neq 0$, then $V_\mu \neq 0$ for some $\mu \in H$;
3. $\operatorname{tr}\bigl(t \mapsto A \circ t \circ T^\vee\bigr) = 2^n \sum_{\mu \in H} \operatorname{tr}(A \mid V_\mu)$.

## Proof

Let $G_{ab}$ be the action of $\mathfrak{gl}_n$ on $E^\vee$ (`exists_dual_lie_family`), and let $E^\vee_\mu$ be its highest weight vectors of weight $\mu$.

1. **Weights.** `dual_weights_dominated`: $E^\vee$ is the sum of its weight spaces, and each weight is below $m_0 = (2\lambda_a + n - 1 - 2a)_{0 \le a < n}$ in the order `DomLE`, which we have not unfolded.
2. **Highest weight vectors go to highest weight vectors.** Each $t$ in the Hom space intertwines $G$ with $K$ (`invariant_intertwines_dual`), so $t(E^\vee_\mu) \subseteq V_\mu$.
3. **Only $H$ occurs** (`hw_harm`). A nonzero $v \in V_\mu$ with $\mu$ below $m_0$ has $\mu \in H$. The proof uses `parthasarathy_rao_varadarajan`, `clifford_highest_weight_vector` and `harmonic_of_norm_bound`, which we have not unfolded.
4. **Decomposition.** By 1 to 3, restriction gives a linear isomorphism
$$R \colon \mathrm{Hom}_{U(n)}(E^\vee, V) \to \prod_{\mu \in H} \mathrm{Hom}(E^\vee_\mu, V_\mu).$$
It is injective by `finite_weights_invariant_hom` and surjective by `exists_invariant_extending`. Under $R$ the action of $A$ becomes $f_\mu \mapsto A \circ f_\mu \circ T^\vee$ on each factor.
5. **Traces.** For $f \mapsto a \circ f \circ b$ on $\mathrm{Hom}(W, H)$ the trace is $\operatorname{tr}(b)\operatorname{tr}(a)$ (`trace_factor_tensor_decomp`). This lemma also gives $\dim V_\mu < \infty$.
6. **The factor $2^n$** (`dualtr`). For $\mu \in H$, $\operatorname{tr}(T^\vee \mid E^\vee_\mu) = 2^n$. Write $\operatorname{tr}(\rho(k)^{-1}T)$ on $E^\vee$ in two ways at $k = \mathrm{diag}(z)$. `dual_weight_trace_formula` gives $\sum_\nu \operatorname{tr}(T^\vee \mid E^\vee_\nu)\,\chi_\nu(z)$, and `twisted_trace_weyl_character` gives $\prod_{a,b}(1 + z_a/z_b)\,\chi_\lambda(z^2)$. `harmonic_weights_coefficient` reads off the coefficient $2^n$ at each $\mu \in H$.

So $E^\vee_\mu \neq 0$ for $\mu \in H$, and parts 1 to 3 follow.

## In the Lean code

The theorem is at [DiagonalMemUnitary.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DiagonalMemUnitary.lean#L112). `CountG` is in [HighestVectorsRegularLine.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/RealLeviDescent/HighestVectorsRegularLine.lean#L63), and `invA`, `flipA`, `hwSp`, `harmSet` and `m0` are in [IsCoreMod.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/RealLeviDescent/IsCoreMod.lean#L95). The proof works with the integer weights `harmZ` and maps them to $H$ by `harmSet_eq` in [WtRInjective.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/WtRInjective.lean#L36). Each `GlobalTheory.T` lemma named above is a statement file that we have not unfolded. The module is named after the helper `diagonal_mem_unitary`, which says that $\mathrm{diag}(z)$ is unitary when $|z_a| = 1$.

The trace `trOn` is 0 on a subspace that is not stable. Part 1 of the statement gives the stability, so the sum in part 3 is a sum of true traces.
