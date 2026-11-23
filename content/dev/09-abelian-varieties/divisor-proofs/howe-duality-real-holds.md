---
id: howe-duality-real-holds
title: Howe duality at the real places, through the Fock model
kind: theorem
decl: GlobalTheory.howeDualityReal_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HoweDualityRealHolds
covers: 433
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `HoweDualityReal`. Its result goes, with no change, to [Howe duality at the real places from the literature](/entry/howe-duality-real-of-literature/), and from there into the bundle of theta inputs of the [literature step](/step/every-character-of-literature/). The proof moves the problem to a tensor product of Fock spaces and quotes a finiteness result there.

## Statement

The statement is given in full in [the entry above](/entry/howe-duality-real-of-literature/). In short: $E/F$ is a CM extension, $X$ is Hermitian of dimension $n$, $W$ is skew-Hermitian of dimension $d$, $\omega$ is a Weil representation of $U(X) \times U(W)$, and Cartan involutions are fixed at the infinite places. Let $\mathrm{Pol}$ be the polynomial Schwartz space at the infinite places. Call $N \subseteq \mathrm{Pol}$ admissible (`ThetaSubInf`) when it contains the image of the Lie algebra of $U(X)_\infty$ and of $k - 1$ for $k \in K_X$, and is stable under the Lie algebra of $U(W)_\infty$ and under $K_W$. Then strictly increasing chains of admissible subspaces have bounded length, and the sum of two proper admissible subspaces is proper.

## Proof

1. **The Fock model.** `exists_frames_fockMap_polynomial_lie_actions` gives, for each infinite place $w$, integers $P_w, Q_w, R_w, S_w$ and an injective linear map $\Phi \colon \bigotimes_w \mathrm{Pol}_w \to \mathrm{Pol}$ with image exactly $\mathrm{Pol}$. Here $\mathrm{Pol}_w$ is the polynomial ring in variables indexed by $(P_w + Q_w) \times (R_w + S_w)$. Under $\Phi$, the actions of the two Lie algebras become the oscillator actions $\mathfrak{gl}_{P_w+Q_w} \to \operatorname{End}(\mathrm{Pol}_w)$ and $\mathfrak{gl}_{R_w+S_w} \to \operatorname{End}(\mathrm{Pol}_w)$, up to constants $c_w$, $c'_w$.
2. **Pull back.** Let $N$ be admissible. Then $\Phi^{-1}(N)$ is stable under each $\mathfrak{gl}_{R_w+S_w}$ (`thetaLift_submodule_comap_stable_secondMember`). It contains $C$, the span of the pure tensors with one factor in $C_w$, where $C_w$ is spanned by the $Z f + c_w \operatorname{tr}(Z) f$ for $Z \in \mathfrak{gl}_{P_w+Q_w}$ (`thetaLift_submodule_contains_firstMember_coinvariants`).
3. **Howe duality in the Fock space.** `howe_duality_characters_fock_tensor_product` says: among the subspaces of $\bigotimes_w \mathrm{Pol}_w$ that contain $C$ and are stable under all $\mathfrak{gl}_{R_w+S_w}$, chains have bounded length, and the sum of two proper ones is proper.
4. **Push forward.** Since $\Phi$ is a bijection onto $\mathrm{Pol}$, $N \mapsto \Phi^{-1}(N)$ preserves strict inclusion, properness and sums. Both conclusions follow. The rest is bookkeeping.

## In the Lean code

The theorem is at [HoweDualityRealHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HoweDualityRealHolds.lean#L18). The statement is at [HoweDualityReal.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/HoweDualityReal.lean#L21).

- The Fock actions `fockAct1`, `fockAct2` are at [DataTheta.lean](lean:Formalism/LocalRingCardinality/DataTheta.lean#L209). The condition `HoweAlg` and the subspaces `coinv`, `tensAny` are at [ActAtApply.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ActAtApply.lean#L84).
- The four lemmas above are second names. They point to `HoweD.FockData.exists_fock_data`, `HoweD.stab_comap_of_thetaSubInf`, `HoweD.tensAny_coinv_le_comap` and `howeAlg_fock_tensor`. We have not unfolded them. The last one carries most of the 433 declarations.
- The four hypotheses `ResEtaPow` and `IsHecke` on $\chi_X$ and $\chi_W$ are introduced as `_` and never used.
- The result in step 3 has no hypothesis on the groups $K_w$: only Lie algebra actions appear. So the $K_X$ and $K_W$ conditions of `ThetaSubInf` can only enter through steps 1 and 2.
